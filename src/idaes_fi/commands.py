"""
CLI commands.

All commands are sub-commands of the command named in
MAIN_COMMAND.
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Optional

from idaes_fi.api import init_report_db, load_module, get_module_flowsheet_runners
from idaes_fi.reportdb import ReportDB
from idaes_fi.reportdb_migrate import MigrationStrategy, MigrationError

__author__ = "Dan Gunter (LBNL)"

# Package name, for help/descriptions
PKG = "IDAES Flowsheet Inspector"

# Main command.
# Stands for "IDAES Flowsheet Inspector"
# Should match value in pyproject.toml under [project.scripts]
MAIN_COMMAND = "ifi"


# ----
# Database commands
# ----


def _get_db(filename: Optional[str] = None) -> ReportDB:
    if filename is None:
        db = init_report_db()
    else:
        db = ReportDB(filename)
    return db


def db_migrate(filename: Optional[str] = None):
    db = _get_db(filename)
    ms = MigrationStrategy()
    ms.migrate(db.filename)


def _db_migrate_cli(args) -> bool:
    try:
        print("Migrating database..")
        did_something = db_migrate(args.file)
    except MigrationError as err:
        print(f"Migration not performed: {err}")
        return False
    if did_something:
        print("Success!")
    else:
        print("Nothing to do, database is already latest version")
    return True


def db_info(filename: Optional[str] = None):
    db = _get_db(filename)
    rdb_ver = ReportDB.MAJOR_VERSION, ReportDB.MINOR_VERSION
    return {"file": db.filename, "version": db.version, "lib_version": rdb_ver}


def _db_info_cli(args) -> bool:
    info = db_info(args.file)
    if args.json:
        json.dump(info, sys.stdout, indent=2, cls=PathJSONEncoder)
    else:
        w = max((len(s) for s in info))
        for k, v in info.items():
            name = k.rjust(w)
            if k.endswith("version"):
                v = f"{v[0]}.{v[1]}"
            print(f"{name}: {v}")
    return True


# ----
# Flowsheet commands
# ----


def _load_flowsheet(modulename: str | None, filename: str | None, varname: str | None):
    if modulename is None and filename is None:
        raise ValueError("Cannot load flowsheet: both module and file are empty")
    try:
        mod = load_module(modulename, filename)
    except ImportError as err:
        which = modulename if modulename else filename
        raise ValueError(f"Could not import flowsheet '{which}': {err}")
    runners = get_module_flowsheet_runners(mod)
    modname = mod.__name__
    if not runners:
        raise KeyError(f"No flowsheets found in module {modname}")
    if varname:
        if not varname in runners:
            raise KeyError(f"Flowsheet {varname} not found in module {modname}")
        return runners[varname]
    elif len(runners) > 1:
        raise KeyError(
            f"Multiple flowsheets in module {modname} but no flowsheet name given"
        )
    return list(runners.values())[0]


def flowsheet_run(
    module: Optional[str] = None,
    file: Optional[str] = None,
    name: Optional[str] = None,
    last_step: Optional[str] = None,
    level: Optional[int] = None,
):
    flowsheet = _load_flowsheet(module, file, name)
    if last_step is not None:
        flowsheet.last_step = last_step
    if level is not None:
        flowsheet.log_level = level
    flowsheet.run_flowsheet()


def _flowsheet_run_cli(args):
    if args.module is None and args.file is None:
        print("Must set --module or --file")
        return False
    try:
        flowsheet_run(
            module=args.module,
            file=args.file,
            name=args.name,
            level=args.level,
            last_step=args.last_step,
        )
    except Exception as err:
        print(f"Could not run flowsheet: {err}")
        return False
    return True


def flowsheet_steps(
    module: Optional[str] = None,
    file: Optional[str] = None,
    name: Optional[str] = None,
):
    flowsheet = _load_flowsheet(module, file, name)
    return flowsheet.steps


def _flowsheet_steps_cli(args):
    if args.module is None and args.file is None:
        print("Must set --module or --file")
        return False
    try:
        steps = flowsheet_steps(module=args.module, file=args.file, name=args.name)
    except Exception as err:
        print(f"Could not load flowsheet to extract steps.\nReason: {err}")
        return False
    if args.json:
        json.dump(steps, sys.stdout)
    else:
        print(", ".join(steps))
    return True


# ----
# Utilities
# ----


class PathJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)


class LogLevelAction(argparse.Action):
    """Parse a case-insensitive logging level name."""

    _levels = {
        "NOTSET": logging.NOTSET,
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARN": logging.WARNING,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "FATAL": logging.CRITICAL,
        "CRITICAL": logging.CRITICAL,
    }

    def __call__(self, parser, namespace, values, option_string=None):
        try:
            level = self._levels[values.upper()]
        except (AttributeError, KeyError):
            choices = ", ".join(self._levels)
            raise argparse.ArgumentError(
                self,
                f"invalid log level: {values!r} (choose from {choices})",
            )
        setattr(namespace, self.dest, level)


# ----
# Main entry point
# ----


def main():
    p = argparse.ArgumentParser(f"{PKG}")
    p_subp = p.add_subparsers()
    # global options
    p.add_argument(
        "--json",
        "-J",
        action="store_true",
        help="Format output as JSON (default=plain text)",
    )

    # add 'db' subcommand and sub-subcommands
    dbp = p_subp.add_parser("db")
    dbp_subp = dbp.add_subparsers()
    # db migrate
    cmd = dbp_subp.add_parser("migrate", help="Migrate to latest database version")
    cmd.set_defaults(func=_db_migrate_cli)
    cmd.add_argument("--file", "-f", help="Database file (instead of default)")
    # db version
    cmd = dbp_subp.add_parser("info", help="Show current database information")
    cmd.add_argument("--file", "-f", help="Database file (instead of default)")
    cmd.set_defaults(func=_db_info_cli)

    # add 'flowsheet' subcommand and sub-subcommands
    runp = p_subp.add_parser("flowsheet")
    runp.add_argument(
        "--level",
        "-L",
        help="Set logging level for flowsheet runner",
        choices=["critical", "fatal", "error", "warn", "warning", "info", "debug"],
        action=LogLevelAction,
        default=logging.INFO,
    )
    run_subp = runp.add_subparsers()
    # run flowsheet
    cmd = run_subp.add_parser("run")
    cmd.add_argument("--file", "-f", help="Flowsheet Python file")
    cmd.add_argument("--module", "-m", help="Flowsheet Python module name")
    cmd.add_argument("--name", "-n", help="Flowsheet variable name (if >1)")
    cmd.add_argument(
        "--last-step", "-l", help="Flowsheet step at which to stop the run"
    )
    cmd.set_defaults(func=_flowsheet_run_cli)
    # get steps for flowsheet
    cmd = run_subp.add_parser("steps")
    cmd.add_argument("--file", "-f", help="Flowsheet Python file")
    cmd.add_argument("--module", "-m", help="Flowsheet Python module name")
    cmd.add_argument("--name", "-n", help="Flowsheet variable name (if >1)")
    cmd.set_defaults(func=_flowsheet_steps_cli)

    args = p.parse_args()
    success = args.func(args)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

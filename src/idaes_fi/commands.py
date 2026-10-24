"""
CLI commands.

All commands are sub-commands of the command named in
MAIN_COMMAND.
"""

import argparse
import sys

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


def _get_db(filename: str | None) -> ReportDB:
    if filename is None:
        db = init_report_db()
    else:
        db = ReportDB(filename)
    return db


def db_migrate(filename: str | None):
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


def db_info(filename: str | None):
    db = _get_db(filename)
    return {"file": db.filename, "version": db.version}


def _db_info_cli(args) -> bool:
    info = db_info(args.file)
    w = max((len(s) for s in info))
    for k, v in info.items():
        name = k.rjust(w)
        if k == "version":
            v = f"{v[0]}.{v[1]}"
        print(f"{name}: {v}")
    return True


# ----
# Flowsheet commands
# ----


def _load_flowsheet(modulename: str | None, filename: str | None, varname: str | None):
    if modulename is None and filename is None:
        raise ValueError("Cannot load flowsheet: both module and file are empty")
    mod = load_module(modulename, filename)
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


def flowsheet_run(modulename, filename, fsname):
    flowsheet = _load_flowsheet(modulename, filename, fsname)
    flowsheet.run_flowsheet()


def _flowsheet_run_cli(args):
    if args.module is None and args.file is None:
        print("Must set --module or --file")
        return False
    try:
        flowsheet_run(args.module, args.file, args.name)
    except Exception as err:
        print(f"Could not run flowsheet: {err}")
        return False
    return True


def flowsheet_steps(modulename, filename, fsname):
    flowsheet = _load_flowsheet(modulename, filename, fsname)
    return flowsheet.steps


def _flowsheet_steps_cli(args):
    if args.module is None and args.file is None:
        print("Must set --module or --file")
        return False
    steps = flowsheet_steps(args.module, args.file, args.name)
    print(", ".join(steps))
    return True


# ----
# Main entry point
# ----


def main():
    p = argparse.ArgumentParser(f"{PKG}")
    p_subp = p.add_subparsers()

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
    run_subp = runp.add_subparsers()
    # run flowsheet
    cmd = run_subp.add_parser("run")
    cmd.add_argument("--file", "-f", help="Flowsheet Python file")
    cmd.add_argument("--module", "-m", help="Flowsheet Python module name")
    cmd.add_argument("--name", "-n", help="Flowsheet variable name (if >1)")
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

"""
New API
"""

# stdlib
import inspect
import json
from pathlib import Path
import sys
import traceback
from typing import Optional

# ext
import sqlite3
from pydantic import BaseModel

# idaes
from idaes.config import get_data_directory
from idaes.logger import getIdaesLogger

# pkg
from .reportdb import ReportDB, DBError
from .action_base import Action
from .common import Steps


class FlowsheetRunner:
    """Flowsheet runner.

    Attributes:
        model: Flowsheet model (provided by caller)
        actions: List of actions to invoke at step begin/end (provided by class)
    """

    def __init__(
        self,
        flowsheet_name: str = "fs",
        report_db: Optional[bool | ReportDB] = True,
        quiet: bool = False,
    ):
        """Constructor.

        Args:
            flowsheet_name: Name in model of flowsheet block
            report_db: If True or None, get default DB. If False, do not
                       use a report db. Otherwise, use value as the report
                       database (assume it is a ReportDB instance).
            quiet: If True, do not print anything to the console (logging
                   may still occur, but that is controlled separately)
        """
        self._quiet = quiet
        if report_db is False:
            self._report_db = None
        else:
            self._report_db = init_report_db()
            self._report_id = None
        self.model = None
        self._fs_name = flowsheet_name

        caller = inspect.currentframe().f_back
        self._caller_file = caller.f_globals.get("__file__") if caller else None
        self.actions: list[Action] = self._default_actions()

        self._idaes_log = getIdaesLogger(__name__, tag="ui")

        self._completed_steps = []

    @property
    def report_db_file(self) -> Path:
        return Path(self._report_db.filename)

    def _default_actions(self) -> list[Action]:
        from .actions import (
            GitHash,
            MermaidDiagram,
            UnitModelReport,
            ModelVariables,
            StreamTable,
            CaptureSolverOutput,
            Diagnostics,
            GetSolverResults,
            Timer,
            UnitDofChecker,
        )

        dof_steps = [Steps.build, Steps.solve_initial, Steps.solve_optimization]

        return [
            clazz(self, *args)
            for clazz, args in (
                (CaptureSolverOutput, ()),
                (Diagnostics, ()),
                (UnitDofChecker, (self._fs_name, dof_steps)),
                (MermaidDiagram, ()),
                (UnitModelReport, ()),
                (ModelVariables, ()),
                #                (GetSolverResults, ()),
                (StreamTable, ()),
                (Timer, ()),
                (GitHash, (self._caller_file,)),
            )
        ]

    def run_flowsheet(self, fn, *args, **kwargs) -> object:
        """Call this with the main entry point of the
        flowsheet, along with any associated arguments.
        This allows capture of errors during execution.
        """
        self._current_step = None
        self._log("begin")

        if self._report_db:
            self._report_id = self._report_db.add_report({})

        # before-run actions
        for action in self.actions:
            action.before_run()

        try:
            run_error, result = None, None
            result = fn(self, *args, **kwargs)
        except Exception as err:
            print(f"Exception! run_error={err}")
            self._log("end", error=err)
            self._current_step = None
            run_error = err
        else:
            self._log("end")

        self._flowsheet_end(error=run_error)

        return result

    def step_begin(self, name: str):
        # close prev step, if needed
        if self._current_step is not None:
            self.step_end()

        # setup
        self._current_step = name
        self._log("begin")

        # run actions
        for action in self.actions:
            action.before_step(self._current_step)

    def step_end(self):
        # checks
        if self.model is None:
            raise ValueError("Must call set_model before end of first step")
        if self._current_step is None:
            raise ValueError("step_end called without matching step_begin")

        # run actions
        for action in self.actions:
            action.after_step(self._current_step)

        # finalize
        self._log("end")
        self._completed_steps.append(self._current_step)
        self._current_step = None

    def _flowsheet_end(self, error=None):
        # close out last step, if needed
        if self._current_step is not None:
            self.step_end()

        # run actions
        for action in self.actions:
            action.after_run()

        report = self._create_report()
        if self._report_db is not None:
            self._save_report(report, error)
        elif not self._quiet:
            self._print_report(report, error)

    def _log(self, stage: str, error=None):
        what = f"flowsheet.{self._current_step}" if self._current_step else "flowsheet"
        msg = f"{what}::{stage}"
        if error is not None:
            msg += ";error={error}"
        self._idaes_log.info(msg)

    def _create_report(self) -> dict[str, dict]:
        """Compile reports of each action into a combined report

        Returns:
            dict: Mapping with two key-value pairs:
                    - `actions`: Keys are names given to actions during `add_action()`, values are the
                      reports returned by that action, in Python dictionary form.
                    - `last_run`: List of steps (names, as strings) in previous run
        """
        # create a mapping of actions to report dicts
        action_reports = {}
        for action in self.actions:
            rpt = action.report()
            rpt_dict = rpt.model_dump() if isinstance(rpt, BaseModel) else rpt
            name = action.name
            action_reports[name] = rpt_dict
        # return actions and other metadata as a report
        return {"actions": action_reports, "last_run": self._completed_steps}

    def _save_report(self, report: dict, error: Optional[Exception] = None):
        if Steps.solve_optimization in self._completed_steps:
            solver_status = True
        else:
            solver_status = False

        if error:
            # build a full error message
            tb = error.__traceback__
            tb_text = "".join(traceback.format_tb(tb))
            error_msg = f"{error.__class__.__name__}: {error}\nTraceback:\n{tb_text}"
            run_status = False
        else:
            error_msg = ""
            run_status = True

        self._report_db.add_report(
            report,
            tags="",
            solver_status=solver_status,
            run_status=run_status,
            run_exc=error_msg,
            update_row_id=self._report_id,
        )

    def _print_report(self, report: dict, error: Optional[Exception] = None):
        if error:
            print(f"ERROR: {error}")
        actions = report["actions"]
        solver_out = actions["CaptureSolverOutput"]["output"]
        for name, output in solver_out.items():
            print(f"--- {name} ---\n{output}\n--- End ({name}) ---")
        # json.dump(report, sys.stdout, indent=2)


def init_report_db() -> ReportDB:
    """Initialize sqlite3 database instance used to record flowsheet
    action reports.Try to create the database if it does not exist.

    Raises:
        DBError: Cannot open/create report database
    """
    report_dir = get_report_db_path()
    if not report_dir.exists():
        raise DBError(
            "while trying to initialize report database: "
            f"parent directory {report_dir} does not exist"
        )
    report_db_path = report_dir / "reportdb.sqlite"
    created = report_db_path.exists()
    db = ReportDB(report_db_path)
    if not created:
        try:
            db.create()
        except sqlite3.Error as err:
            raise DBError(
                "while trying to create new report database"
                f" at {report_db_path}: {err}"
            )

    # test that DB is valid, raising DBError if not
    db.test_connection()

    return db


def get_report_db_path() -> Path:
    """Compute and return the default path to the report database."""
    data_dir, _, _ = get_data_directory()
    return Path(data_dir)

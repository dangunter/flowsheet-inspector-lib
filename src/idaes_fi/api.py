######################################################################################################
# Process Optimization and Modeling for Minerals Sustainability (PrOMMiS) Copyright (c) 2023-2026
#
# “Process Optimization and Modeling for Minerals Sustainability (PrOMMiS)” was produced under the DOE
# Process Optimization and Modeling for Minerals Sustainability (“PrOMMiS”) initiative, and is
# copyrighted by the software owners: The Regents of the University of California, through Lawrence
# Berkeley National Laboratory, National Technology & Engineering Solutions of Sandia, LLC through
# Sandia National Laboratories, Carnegie Mellon University, University of Notre Dame, and West
# Virginia University Research Corporation.
#
# NOTICE. This Software was developed under funding from the U.S. Department of Energy and the
# U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted
# for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license
# in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform
# publicly and display publicly, and to permit other to do so.
#
######################################################################################################

"""
Main API for using IDAES-PSE flowsheets with the Flowsheet Inspector.
"""

# stdlib
from abc import ABC, abstractmethod
import inspect
import importlib
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys
import time
import traceback
from types import ModuleType
from typing import Callable, Optional

# ext
import sqlite3
from pydantic import BaseModel

# idaes-pse
from idaes.config import get_data_directory
from idaes.logger import getIdaesLogger

# pkg
from .reportdb import ReportDB, DBError
from .action_base import Action
from .common import Steps

__author__ = "Dan Gunter (LBNL)"


class _FlowsheetRunnerInterface(ABC):
    @abstractmethod
    def run_flowsheet(self, *args, **kwargs) -> object:
        pass

    @abstractmethod
    def step_begin(self, name: str):
        pass

    @abstractmethod
    def step_end(self):
        pass

    @abstractmethod
    def _get_main(self) -> Optional[Callable]:
        pass

    @abstractmethod
    def _set_main(self, fn: Optional[Callable]):
        pass

    main = property(_get_main, _set_main)

    @abstractmethod
    def _get_report_db_file(self) -> Path:
        pass

    report_db_file = property(_get_report_db_file, None)

    @abstractmethod
    def _get_model(self) -> object:
        pass

    @abstractmethod
    def _set_model(self, m: object):
        pass

    model = property(_get_model, _set_model)

    @abstractmethod
    def _get_steps(self) -> list[str]:
        pass

    @abstractmethod
    def _set_steps(self, s: list[str]):
        pass

    steps = property(_get_steps, _set_steps)


class FlowsheetRunner(_FlowsheetRunnerInterface):
    """For using your flowsheet with the Flowsheet Inspector."""

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
        self._fs_name = flowsheet_name
        self._model = None
        self._steps = None
        self._main = None

        caller = inspect.currentframe().f_back
        self._caller_file = caller.f_globals.get("__file__") if caller else None
        self.actions: list[Action] = self._default_actions()

        self._idaes_log = getIdaesLogger(__name__, tag="ui")

        self._completed_steps = []

    def _get_report_db_file(self) -> Path:
        return Path(self._report_db.filename)

    #: Get report database file path
    report_db_file = property(_get_report_db_file, None)

    def _get_model(self) -> object:
        return self._model

    def _set_model(self, m: object):
        self._model = m

    #: Get/set the model
    model = property(_get_model, _set_model)

    def _get_steps(self) -> list[str]:
        if self._steps is None:
            return []
        return self._steps

    def _set_steps(self, s: list[str]):
        self._steps = s

    # Get/set the list of steps
    steps = property(_get_steps, _set_steps)

    def _get_main(self) -> Optional[Callable]:
        return self._main

    def _set_main(self, fn: Optional[Callable]):
        if fn is not None and not callable(fn):
            raise TypeError("main must be callable or None")
        self._main = fn

    # Get/set the main flowsheet function
    main = property(_get_main, _set_main)

    def _default_actions(self) -> list[Action]:
        from .actions import (
            GitHash,
            MermaidDiagram,
            UnitModelReport,
            ModelVariables,
            StreamTable,
            CaptureSolverOutput,
            Diagnostics,
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

    def run_flowsheet(self, *args, **kwargs) -> object:
        """Run the flowsheet, passing arguments to function provided as `main`."""
        if self._main is None:
            raise ValueError("Must set .main function before calling run_flowsheet")

        self._current_step = None
        self._log("begin")

        if self._report_db:
            self._report_id = self._report_db.add_report({})

        # before-run actions
        for action in self.actions:
            action.before_run()

        try:
            run_error, result = None, None
            result = self._main(self, *args, **kwargs)
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


class NullFlowsheetRunner(_FlowsheetRunnerInterface):
    """Abstract (cannot be instantiated) interface for the
    FlowsheetRunner class. For use of the Null object design
    pattern; see NullFlowsheetRunner class.
    """

    def run_flowsheet(self, fn, *args, **kwargs) -> object:
        return fn(self, *args, **kwargs)

    def step_begin(self, name: str):
        pass

    def step_end(self):
        pass

    def _get_main(self) -> Optional[Callable]:
        return None

    def _set_main(self, fn: Optional[Callable]):
        pass

    def _get_report_db_file(self) -> Path:
        return Path()

    def _get_model(self) -> object:
        return None

    def _set_model(self, m: object):
        pass

    def _get_steps(self) -> list[str]:
        return []

    def _set_steps(self, s: list[str]):
        pass

    report_db_file = property(_get_report_db_file, None)
    model = property(_get_model, _set_model)
    steps = property(_get_steps, _set_steps)
    main = property(_get_main, _set_main)


## report db helper functions


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


def get_module_flowsheet_runners(m: ModuleType) -> dict[str, _FlowsheetRunnerInterface]:
    """Get list of variables in a module that are FlowsheetRunner-s."""
    result = {}
    for key in dir(m):
        v = m[key]
        if issubclass(v, _FlowsheetRunnerInterface):
            result[key] = v
    return result


def load_module(name, path):
    if name:
        module = importlib.import_module(name)
    else:
        path = Path(path).resolve()
        name = path.stem
        spec = spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load module from {path}")
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


def run_flowsheet(
    module_name: Optional[str] = None,
    path: Optional[Path] = None,
    flowsheet_name: Optional[str] = "FS",
):
    """Run specified flowsheet (or only one) in specified module."""
    module = load_module(module_name, path)
    runners = get_module_flowsheet_runners(module)
    if len(runners) == 0:
        raise ValueError(f"No FlowsheetRunner-s found in module '{module.__name__}'")
    if len(runners) == 1:
        runner = list(runners.values())[0]
    else:
        runner = runners.get(flowsheet_name, None)
        if runner is None:
            raise KeyError(
                f"No flowsheet '{flowsheet_name}' in module '{module.__name__}'"
            )
    return runner.run_flowsheet()

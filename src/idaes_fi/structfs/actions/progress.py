"""
Action to report progress of a flowsheet run.
"""

# stdlib
from enum import Enum
import os
import time
import traceback

# package
from ..action_base import Action

# third-party
from pydantic import BaseModel


class Status(str, Enum):
    """Status of a step in a flowsheet run."""

    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Progress(Action):
    """Action to track the progress of a run."""

    class Report(BaseModel):
        """Stream table, where each row is a variable and each column is a stream."""

        steps: dict[str, dict[str, object]]  # one dict per step

    def __init__(self, runner, **kwargs):
        super().__init__(runner, **kwargs)
        self._progress = {}
        self._time = {}

    def before_step(self, step_name: str):
        """Record progress before a step is run."""
        start_time = time.time()
        self._progress[step_name] = {
            "status": Status.RUNNING.value,
            "start_time": start_time,
        }
        self._time[step_name] = start_time

    def after_step(self, step_name: str):
        """Record progress after a step is run."""
        record = self._progress[step_name]
        record["status"] = Status.COMPLETED.value
        record["duration"] = time.time() - self._time[step_name]

    def step_failed(self, step_name: str, error: Exception):
        """Record progress after a step fails."""
        record = self._progress[step_name]
        record["status"] = Status.FAILED.value
        record["duration"] = time.time() - self._time[step_name]
        record["error"] = str(error)
        record["traceback"] = self._format_tb(error)
        record["environment"] = os.environ.copy()

    def _format_tb(self, e: Exception) -> str:
        tb_list = traceback.format_tb(e.__traceback__)
        return tb_list

    def report(self) -> Report:
        return self.Report(steps=self._progress)

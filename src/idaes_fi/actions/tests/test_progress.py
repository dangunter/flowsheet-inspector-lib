#################################################################################
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
#################################################################################

"""
Tests for the Progress action.
"""

from types import SimpleNamespace
import sqlite3

import pytest

from idaes_fi.api import FlowsheetRunner, Steps
from idaes_fi.reportdb import ReportDB
from idaes_fi.actions.progress import Progress, Status, StepInfo
from idaes_fi.tests import demo_flowsheet


@pytest.fixture
def runner():
    r = SimpleNamespace()
    r._reportdb = SimpleNamespace()
    r._reportdb.add_status = lambda *args, **kwargs: None
    return r


@pytest.mark.unit
def test_progress_smoke(runner):
    p = Progress(runner)
    si = StepInfo(name="foo", number=1, status=Status.RUNNING, start=0.0)


@pytest.mark.unit
def test_progress_api(runner):
    p = Progress(runner)
    p.before_run()
    p.before_step("step1")
    p.before_step("solve_step")  # will trigger solver logic
    p.before_step("step3")
    p.after_run()


@pytest.mark.integration
def test_progress_flowsheet(tmp_path):
    db = tmp_path / "report.sqlite"
    runner = demo_flowsheet.runner
    runner.report_db_file = db
    runner.main = progress_main
    print(f"demo flowsheet with temp db '{db}'")
    runner.run_flowsheet()  # rest of checks are in this function


def progress_main(runner: FlowsheetRunner):
    # check that the run id is set in the actions
    rid = None
    for a in runner.actions:
        assert a.run_id is not None
        if rid is None:
            rid = a.run_id
        else:
            # they should all be the same
            assert rid == a.run_id
    # finish one step
    runner.model = demo_flowsheet.build_flowsheet()
    runner.step_end(Steps.build)
    # double-check that run id is still the same
    for a in runner.actions:
        assert a.run_id is not None
        assert rid == a.run_id
    # there should be a single row in the status table
    # with this run id
    with sqlite3.connect(runner.report_db_file) as conn:
        n = 0
        for row in conn.execute(f"SELECT * FROM {ReportDB.STAT_TABLE}"):
            assert n == 0  # should not be > 1 row
            run_id = row[1]
            assert run_id == rid
            n += 1
    # do another step
    demo_flowsheet.step_end(Steps.set_scaling)
    # now there should be 2 rows with that run id
    with sqlite3.connect(runner.report_db_file) as conn:
        n = 0
        for row in conn.execute(f"SELECT * FROM {ReportDB.STAT_TABLE}"):
            assert n < 2
            run_id = row[1]
            assert run_id == rid
            n += 1

    # that's it, we're done!

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

import pytest

from idaes_fi.actions.progress import Progress, Status, StepInfo


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

"""
Test for the solver action.
"""

from idaes_fi.structfs import FlowsheetRunner, Steps
from idaes_fi.structfs.tests.demo_flowsheet import *

import pytest

_stages = []
_solver_name = "couenne"

##############################
# Create a wrapped flowsheet #
##############################

FS = FlowsheetRunner(
    name="Demo Flowsheet with Couenne",
    tags="test demo couenne",
    module="idaes_fi.structfs.actions.tests.test_solver",
)


@FS.step(Steps.build)
def build(ctx):
    ctx.model = build_flowsheet()
    _stages.append(Steps.build)


@FS.step(Steps.set_operating_conditions)
def set_operating_conditions(ctx):
    set_dof(ctx.model)
    _stages.append(Steps.set_operating_conditions)


@FS.step(Steps.set_scaling)
def runner_set_scaling(ctx):
    set_scaling(ctx.model)
    _stages.append(Steps.set_scaling)


@FS.step(Steps.solve_initial)
def solve_initial(ctx):
    initialize_flowsheet(ctx.model)
    _stages.append(Steps.solve_initial)


@FS.step(Steps.set_solver)
def set_solver(ctx):
    ctx.solver = get_solver(_solver_name)
    _stages.append(Steps.set_solver)


@FS.step(Steps.solve_optimization)
def runner_solve_flowsheet(ctx):
    ctx.results = solve_flowsheet(ctx.model, ctx.solver, stee=True)
    _stages.append(Steps.solve_optimization)


#########
# Tests #
#########


@pytest.mark.integration
def test_solver_action():
    """Test the solver action."""
    global _solver_name

    for name in "couenne", "doesnotexistandneverwill":
        _solver_name = name
        FS.run_steps(first=Steps.build, last=Steps.solve_optimization)
        actions = FS.report()["actions"]
        for step, value in actions["progress"]["steps"].items():
            if value["status"] == "failed":
                print(f"Step failed: {step}: {value['error']}")
                assert False
        assert set(_stages) == {
            Steps.build,
            Steps.set_operating_conditions,
            Steps.set_scaling,
            Steps.solve_initial,
            Steps.set_solver,
            Steps.solve_optimization,
        }

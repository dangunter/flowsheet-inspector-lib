import logging
import sys

import pytest

from idaes_fi import api
from idaes.logger import set_log_tags
from idaes_fi.tests import demo_flowsheet


@pytest.mark.unit
def test_null():
    def say_hello(runner):
        return f"hello {runner}"

    runner = api.NullFlowsheetRunner()
    runner.main = say_hello
    runner.model = "not really a model"
    assert runner.model == "not really a model"
    result = runner.run_flowsheet()
    assert result == f"hello {runner}"


@pytest.mark.unit
def test_log_level():
    steps = ("a", "b")
    runner = api.FlowsheetRunner(steps=steps, report_db=False, quiet=True)

    def noop(runner):
        runner.step_begin("a")
        runner.model = demo_flowsheet.build_flowsheet()
        runner.step_begin("b")

    runner.main = noop
    runner.log_level = logging.INFO
    set_log_tags(("ui",))
    runner.run_flowsheet()


@pytest.mark.unit
def test_last_step(tmp_path):
    steps = ("a", "b", "c", "d")
    runner = api.FlowsheetRunner(steps=steps, report_db=tmp_path / "runner.db")
    where = None

    def mymain(runner):
        runner.step_begin("a")
        where.append("a")
        runner.model = demo_flowsheet.build_flowsheet()
        runner.step_begin("b")
        where.append("b")
        runner.step_begin("c")
        where.append("c")
        runner.step_begin("d")
        where.append("d")

    runner.main = mymain
    print("\nStep: ", end="")  # dbg
    sys.stdout.flush()
    for step_name in "abcd":
        print(f"{step_name}", end=" -> ")  # dbg
        sys.stdout.flush()
        where = []
        runner.last_step = step_name
        runner.run_flowsheet()
        assert where[-1] == step_name
    print("done.")


@pytest.mark.integration
@pytest.mark.parametrize(
    "quiet,report_db", [(True, True), (False, False), (True, False)]
)
def test_demo_flowsheet(tmp_path, quiet, report_db):
    print(f"quiet={quiet} report_db={report_db}")
    if report_db:
        report_db = tmp_path / "test_api_demo_flowsheet_db.sqlite"
    runner = api.FlowsheetRunner(
        steps=(
            api.Steps.build,
            api.Steps.set_scaling,
            api.Steps.initialize,
            api.Steps.set_solver,
            api.Steps.solve_optimization,
        ),
        report_db=report_db,
        quiet=quiet,
    )
    runner.main = fs_main
    runner.run_flowsheet()


def fs_main(runner):
    runner.step_begin(api.Steps.build)
    runner.model = m = demo_flowsheet.build_flowsheet()

    runner.step_begin(api.Steps.set_scaling)
    demo_flowsheet.set_scaling(m)
    runner.step_end()

    demo_flowsheet.set_dof(m)

    runner.step_begin(api.Steps.initialize)
    demo_flowsheet.initialize_flowsheet(m)

    runner.step_begin(api.Steps.set_solver)
    solver = demo_flowsheet.get_solver()

    runner.step_begin(api.Steps.solve_optimization)
    demo_flowsheet.solve_flowsheet(m, solver, stee=True)

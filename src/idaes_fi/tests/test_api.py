import pytest
from idaes_fi import api
from . import demo_flowsheet


def test_api_demo_flowsheet_db(tmp_path):
    report_file = tmp_path / "test_api_demo_flowsheet_db.sqlite"
    db = api.ReportDB(report_file)
    runner = api.FlowsheetRunner(report_db=db)
    runner.main = fs_main
    runner.run_flowsheet()


# @pytest.mark.parametrize("quiet", (True, False))
def test_api_demo_flowsheet_console():
    quiet = False
    print(f"CONSOLE run quiet={quiet}")
    runner = api.FlowsheetRunner(report_db=False, quiet=quiet)
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

import pytest
from idaes_fi.structfs import api
from . import demo_flowsheet


def test_api_demo_flowsheet_db(tmp_path):
    report_file = tmp_path / "test_api_demo_flowsheet_db.sqlite"
    db = api.ReportDB(report_file)
    api.FlowsheetRunner().run_flowsheet(fs_main)


# @pytest.mark.parametrize("quiet", (True, False))
def test_api_demo_flowsheet_console():
    quiet = False
    print(f"CONSOLE run quiet={quiet}")
    api.FlowsheetRunner(report_db=False, quiet=quiet).run_flowsheet(fs_main)


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


#    demo_flowsheet.display_results(m)

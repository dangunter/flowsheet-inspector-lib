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
Import functions from demo flowsheet, call them in a main()
function driven by the lightweight FlowsheetRunner API.
"""

from .. import FlowsheetRunner, Steps
from .demo_flowsheet import *


def main(dbfile=None):
    runner = FlowsheetRunner(
        steps=[
            Steps.build,
            Steps.set_scaling,
            Steps.initialize,
            Steps.set_solver,
            Steps.solve_optimization,
        ],
        report_db=dbfile if dbfile is not None else False,
    )
    runner.main = _main
    return runner.run_flowsheet()


def _main(runner):
    model = build_flowsheet()
    runner.step_begin(Steps.build)
    runner.model = model
    runner.step_begin(Steps.set_scaling)
    set_dof(model)
    set_scaling(model)
    runner.step_begin(Steps.initialize)
    initialize_flowsheet(model)
    runner.step_begin(Steps.set_solver)
    solver = get_solver("ipopt")
    runner.step_begin(Steps.solve_optimization)
    results = solve_flowsheet(model, solver, stee=True)
    return model, results


if __name__ == "__main__":
    main()

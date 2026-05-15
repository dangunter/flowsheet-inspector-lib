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
Import functions from demo flowsheet and wrap them with the FlowsheetRunner
"""

from idaes_fi.structfs.fsrunner import FlowsheetRunner, Steps
from idaes_fi.structfs.tests.demo_flowsheet import *

FS = FlowsheetRunner(name="Demo Flowsheet 2", tags="test demo", module=__name__)


@FS.step(Steps.build)
def build(ctx):
    ctx.model = build_flowsheet()


@FS.step(Steps.set_operating_conditions)
def set_operating_conditions(ctx):
    set_dof(ctx.model)


@FS.step(Steps.set_scaling)
def runner_set_scaling(ctx):
    set_scaling(ctx.model)


@FS.step(Steps.solve_initial)
def solve_initial(ctx):
    initialize_flowsheet(ctx.model)


@FS.step(Steps.set_solver)
def set_solver(ctx):
    ctx.solver = get_solver("ipopt")


@FS.step(Steps.solve_optimization)
def runner_solve_flowsheet(ctx):
    ctx.results = solve_flowsheet(ctx.model, ctx.solver, stee=True)


FS2 = FlowsheetRunner(name="Demo Flowsheet", tags="test demo", module=__name__)


@FS2.step(Steps.build)
def build(ctx):
    ctx.model = build_flowsheet()


@FS2.step(Steps.set_operating_conditions)
def set_operating_conditions(ctx):
    set_dof(ctx.model)


@FS2.step(Steps.set_scaling)
def runner_set_scaling(ctx):
    set_scaling(ctx.model)


@FS2.step(Steps.solve_initial)
def solve_initial(ctx):
    initialize_flowsheet(ctx.model)


@FS2.step(Steps.set_solver)
def set_solver(ctx):
    ctx.solver = get_solver("ipopt")


@FS2.step(Steps.solve_optimization)
def runner_solve_flowsheet(ctx):
    ctx.results = solve_flowsheet(ctx.model, ctx.solver, stee=True)


FS3 = FlowsheetRunner(name="Demo Flowsheet 3", tags="test demo", module=__name__)


@FS3.step(Steps.build)
def build(ctx):
    ctx.model = build_flowsheet()


@FS3.step(Steps.set_solver)
def set_solver(ctx):
    ctx.solver = get_solver("ipopt")


@FS3.step(Steps.solve_optimization)
def runner_solve_flowsheet(ctx):
    ctx.results = solve_flowsheet(ctx.model, ctx.solver, stee=True)


if __name__ == "__main__":
    FS.run_steps()

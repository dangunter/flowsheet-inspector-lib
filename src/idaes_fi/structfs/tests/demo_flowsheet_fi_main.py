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
function decorated with @fi_main
"""

from .. import fi_main
from .demo_flowsheet import *


@fi_main(name="Demo Flowsheet")
def main():
    model = build_flowsheet()
    set_dof(model)
    set_scaling(model)
    initialize_flowsheet(model)
    solver = get_solver("ipopt")
    results = solve_flowsheet(model, solver, stee=True)
    return model, results


if __name__ == "__main__":
    main()

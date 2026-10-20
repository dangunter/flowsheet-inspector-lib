---
title: Flowsheet Inspector Library API
---
# Flowsheet Inspector Library API

This section describes the application programming interface (API) used to
"wrap" flowsheets with the Flowsheet Inspector (FI).

## Overview

FI instruments an ordinary IDAES flowsheet by placing its build, setup,
initialization, and solve operations inside named steps. A wrapped flowsheet
has three parts:

1. A `FlowsheetRunner` instance, usually created at module scope.
2. A `main(runner)` function that performs the flowsheet work.
3. Calls to `runner.step_begin()` and `runner.step_end()` around meaningful
   operations.

The runner passes itself to `main`. Assign the constructed Pyomo model to
`runner.model` during the build step so FI's reporting actions can inspect it.
The value returned by `main` is returned by `runner.run_flowsheet()`.

## Minimal wrapper

The following is the basic pattern for an IDAES flowsheet module. The model
construction and solver code are ordinary IDAES/Pyomo code; only the runner
and step calls are FI-specific.

```{code} python
from pyomo.environ import ConcreteModel
from idaes.core import FlowsheetBlock
from idaes.core.solvers import get_solver

from idaes_fi import FlowsheetRunner, Steps


runner = FlowsheetRunner()
runner.steps = [
    Steps.build,
    Steps.initialize,
    Steps.set_solver,
    Steps.solve_optimization,
]


def build_flowsheet():
    model = ConcreteModel()
    model.fs = FlowsheetBlock(dynamic=False)
    # Add the property package, unit models, arcs, and constraints here.
    return model


def main(runner):
    runner.step_begin(Steps.build)
    runner.model = model = build_flowsheet()

    runner.step_begin(Steps.initialize)
    # Initialize units and propagate states as required by the flowsheet.

    runner.step_begin(Steps.set_solver)
    solver = get_solver()

    runner.step_begin(Steps.solve_optimization)
    solver.solve(model, tee=True)
    return model


runner.main = main


if __name__ == "__main__":
    model = runner.run_flowsheet()
```

`step_begin()` closes the previous open step automatically. FI also closes the
last open step when `run_flowsheet()` finishes, so explicit `step_end()` calls
are needed only when some code should be executed that is not part of any step.
For example, the scaling step in the test flowsheet is explicitly closed
so that the `set_degrees_of_freedom()` function is not inside either the
scaling step or the subsequent initialization step:

```{code} python
runner.step_begin(Steps.set_scaling)
set_scaling(model)
runner.step_end()

set_degrees_of_freedom(model)
runner.step_begin(Steps.initialize)
initialize_flowsheet(model)
```

You must set some of the attributes in the FlowsheetRunner object, which
we will call `runner` in these examples, at certain times:

* Before calling `runner.run_flowsheet()`, set the `runner.main` attribute to the
  main function that does all the flowsheet setup and solving. This is allows external
  programs (i.e., the Flowsheet Inspector UI) to re-run the flowsheet programmatically.
* The first step, whatever it is called (typically, `Steps.build`), must set the
  model by assigning `runner.model` to the Pyomo model, before it ends. This is
  necessary to allow subsequent steps to inspect and use the model object.

## Running a wrapped module

Run a module directly from Python with:

```{code} python
from my_flowsheet import runner

model = runner.run_flowsheet()
```

Alternatively, use the API loader. It accepts either an importable module name
or a filesystem path:

```{code} python
from pathlib import Path
from idaes_fi.api import run_flowsheet

run_flowsheet(module_name="my_flowsheet")
run_flowsheet(path=Path("my_flowsheet.py"))
```

`run_flowsheet()` discovers `FlowsheetRunner` instances in the loaded module.
If the module contains one runner, it is selected automatically. If it
contains multiple runners, pass `flowsheet_name` with the runner variable's
name, for example `flowsheet_name="FS2"`.

```{code} python
run_flowsheet(path=Path("flowsheets.py"), flowsheet_name="FS2")
```

The `flowsheet_name` argument to the `FlowsheetRunner` constructor has a
different purpose: it names the flowsheet block in the Pyomo model and is
used by FI actions such as degree-of-freedom checks. It defaults to `"fs"`.

## Steps

Use the constants in `Steps` instead of spelling step names manually. The
available names include:

```{code} python
Steps.build
Steps.set_solver
Steps.initialize
Steps.set_operating_conditions
Steps.set_scaling
Steps.solve_initial
Steps.set_autoscaling
Steps.add_costing
Steps.initialize_costing
Steps.setup_optimization
Steps.solve_optimization
```

The `runner.steps` list records the steps used by the flowsheet and lets FI
actions interpret the run. It does not execute those steps; execution remains
the responsibility of `main`.

## Reports and console output

By default, `FlowsheetRunner` writes FI action reports to the IDAES report
database. Use `report_db=False` to disable database reporting. When database
reporting is disabled, `quiet=False` prints the captured solver output and
errors at the end of the run; `quiet=True` suppresses that report.

To use a specific database, pass a `ReportDB` instance:

```{code} python
from pathlib import Path
from idaes_fi import FlowsheetRunner
from idaes_fi.api import ReportDB

runner = FlowsheetRunner(
    report_db=ReportDB(Path("reports.sqlite")),
    quiet=False,
)
```

The default action set collects solver output, diagnostics, unit-model and
variable reports, stream tables, timings, a Mermaid diagram, and the Git hash
when available. The runner's `report_db_file` property identifies the active
database when database reporting is enabled.

## Complete flow

The test example in `src/idaes_fi/tests/demo_flowsheet.py` follows this
sequence:

```{code} text
build -> set_scaling -> initialize -> set_solver -> solve_optimization
```

Its `main` function builds the benzene/toluene IDAES model, applies scaling,
sets degrees of freedom, initializes the units, obtains a solver, and solves
the model. This is a useful template for adapting an existing IDAES
flowsheet: keep the existing model operations, then add the runner assignment
and step boundaries around them.

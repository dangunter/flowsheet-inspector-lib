# {py:mod}`idaes_fi.structfs.fsrunner`

```{py:module} idaes_fi.structfs.fsrunner
```

```{autodoc2-docstring} idaes_fi.structfs.fsrunner
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Context <idaes_fi.structfs.fsrunner.Context>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context
    :summary:
    ```
* - {py:obj}`BaseFlowsheetRunner <idaes_fi.structfs.fsrunner.BaseFlowsheetRunner>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner
    :summary:
    ```
* - {py:obj}`DiagnosticReportType <idaes_fi.structfs.fsrunner.DiagnosticReportType>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.DiagnosticReportType
    :summary:
    ```
* - {py:obj}`FlowsheetRunner <idaes_fi.structfs.fsrunner.FlowsheetRunner>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`run_flowsheet <idaes_fi.structfs.fsrunner.run_flowsheet>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.run_flowsheet
    :summary:
    ```
* - {py:obj}`_module_target <idaes_fi.structfs.fsrunner._module_target>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner._module_target
    :summary:
    ```
* - {py:obj}`_find_wrapped_main <idaes_fi.structfs.fsrunner._find_wrapped_main>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner._find_wrapped_main
    :summary:
    ```
* - {py:obj}`main <idaes_fi.structfs.fsrunner.main>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner.main
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_log <idaes_fi.structfs.fsrunner._log>`
  - ```{autodoc2-docstring} idaes_fi.structfs.fsrunner._log
    :summary:
    ```
````

### API

````{py:data} _log
:canonical: idaes_fi.structfs.fsrunner._log
:value: >
   'getLogger(...)'

```{autodoc2-docstring} idaes_fi.structfs.fsrunner._log
```

````

`````{py:class} Context()
:canonical: idaes_fi.structfs.fsrunner.Context

Bases: {py:obj}`dict`

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.__init__
```

````{py:property} model
:canonical: idaes_fi.structfs.fsrunner.Context.model

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.model
```

````

````{py:property} solver
:canonical: idaes_fi.structfs.fsrunner.Context.solver

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.solver
```

````

````{py:method} solve()
:canonical: idaes_fi.structfs.fsrunner.Context.solve

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.solve
```

````

````{py:property} tee
:canonical: idaes_fi.structfs.fsrunner.Context.tee

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.tee
```

````

````{py:property} results
:canonical: idaes_fi.structfs.fsrunner.Context.results
:type: dict

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.Context.results
```

````

`````

`````{py:class} BaseFlowsheetRunner(solver=None, tee=True, solver_options: dict | None = None, steps: typing.Sequence[str] = None, **target_kw)
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner

Bases: {py:obj}`idaes_fi.structfs.runner.Runner`

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.__init__
```

````{py:attribute} _SET_SOLVER_STEP
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._SET_SOLVER_STEP
:value: >
   'set_solver'

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._SET_SOLVER_STEP
```

````

````{py:attribute} STEPS
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.STEPS
:value: >
   ()

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.STEPS
```

````

````{py:method} set_solve_steps(solve_steps: typing.Sequence[str])
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.set_solve_steps

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.set_solve_steps
```

````

````{py:method} run_steps(first: str = Runner.STEP_ANY, last: str = Runner.STEP_ANY, before=None, after=None, **kwargs)
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.run_steps

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.run_steps
```

````

````{py:method} _set_solver()
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._set_solver

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._set_solver
```

````

````{py:method} reset()
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.reset

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.reset
```

````

````{py:method} _create_model()
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._create_model

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner._create_model
```

````

````{py:property} model
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.model

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.model
```

````

````{py:property} results
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.results

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.results
```

````

````{py:method} annotate_var(variable: object, key: str = None, title: str = None, desc: str = None, units: str = None, rounding: int = 3, is_input: bool = True, is_output: bool = True, input_category: str = 'main', output_category: str = 'main') -> object
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.annotate_var

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.annotate_var
```

````

````{py:property} annotated_vars
:canonical: idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.annotated_vars
:type: dict[str]

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.BaseFlowsheetRunner.annotated_vars
```

````

`````

`````{py:class} DiagnosticReportType(*args, **kwds)
:canonical: idaes_fi.structfs.fsrunner.DiagnosticReportType

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.DiagnosticReportType
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.DiagnosticReportType.__init__
```

````{py:attribute} STRUCTURAL
:canonical: idaes_fi.structfs.fsrunner.DiagnosticReportType.STRUCTURAL
:value: >
   'structural'

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.DiagnosticReportType.STRUCTURAL
```

````

````{py:attribute} NUMERICAL
:canonical: idaes_fi.structfs.fsrunner.DiagnosticReportType.NUMERICAL
:value: >
   'numerical'

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.DiagnosticReportType.NUMERICAL
```

````

`````

`````{py:class} FlowsheetRunner(solve_steps: list[str] = None, **kwargs)
:canonical: idaes_fi.structfs.fsrunner.FlowsheetRunner

Bases: {py:obj}`idaes_fi.structfs.fsrunner.BaseFlowsheetRunner`

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner.__init__
```

````{py:method} build()
:canonical: idaes_fi.structfs.fsrunner.FlowsheetRunner.build

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner.build
```

````

````{py:method} solve_initial()
:canonical: idaes_fi.structfs.fsrunner.FlowsheetRunner.solve_initial

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner.solve_initial
```

````

````{py:method} show_diagram()
:canonical: idaes_fi.structfs.fsrunner.FlowsheetRunner.show_diagram

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner.show_diagram
```

````

````{py:property} solver_status
:canonical: idaes_fi.structfs.fsrunner.FlowsheetRunner.solver_status
:type: str

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.FlowsheetRunner.solver_status
```

````

`````

````{py:function} run_flowsheet(module_or_path: str, fs_attr: str = '', step_kw: dict[str, str] = None, report_db_file: str = None, **kwargs) -> idaes_fi.structfs.fsrunner.BaseFlowsheetRunner
:canonical: idaes_fi.structfs.fsrunner.run_flowsheet

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.run_flowsheet
```
````

````{py:function} _module_target(mod)
:canonical: idaes_fi.structfs.fsrunner._module_target

```{autodoc2-docstring} idaes_fi.structfs.fsrunner._module_target
```
````

````{py:function} _find_wrapped_main(a_module) -> types.FunctionType | None
:canonical: idaes_fi.structfs.fsrunner._find_wrapped_main

```{autodoc2-docstring} idaes_fi.structfs.fsrunner._find_wrapped_main
```
````

````{py:function} main(args=None)
:canonical: idaes_fi.structfs.fsrunner.main

```{autodoc2-docstring} idaes_fi.structfs.fsrunner.main
```
````

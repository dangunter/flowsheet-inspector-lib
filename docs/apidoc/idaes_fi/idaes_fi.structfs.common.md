# {py:mod}`idaes_fi.structfs.common`

```{py:module} idaes_fi.structfs.common
```

```{autodoc2-docstring} idaes_fi.structfs.common
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ActionNames <idaes_fi.structfs.common.ActionNames>`
  -
* - {py:obj}`Steps <idaes_fi.structfs.common.Steps>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.Steps
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`load_module <idaes_fi.structfs.common.load_module>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.load_module
    :summary:
    ```
* - {py:obj}`find_flowsheet_objects <idaes_fi.structfs.common.find_flowsheet_objects>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.find_flowsheet_objects
    :summary:
    ```
* - {py:obj}`_get_steps_for_flowsheet <idaes_fi.structfs.common._get_steps_for_flowsheet>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common._get_steps_for_flowsheet
    :summary:
    ```
* - {py:obj}`main <idaes_fi.structfs.common.main>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.main
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_SOLVER_NAME <idaes_fi.structfs.common.DEFAULT_SOLVER_NAME>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.DEFAULT_SOLVER_NAME
    :summary:
    ```
* - {py:obj}`RESULT_FLOWSHEET_KEY <idaes_fi.structfs.common.RESULT_FLOWSHEET_KEY>`
  - ```{autodoc2-docstring} idaes_fi.structfs.common.RESULT_FLOWSHEET_KEY
    :summary:
    ```
````

### API

````{py:data} DEFAULT_SOLVER_NAME
:canonical: idaes_fi.structfs.common.DEFAULT_SOLVER_NAME
:value: >
   'ipopt'

```{autodoc2-docstring} idaes_fi.structfs.common.DEFAULT_SOLVER_NAME
```

````

````{py:data} RESULT_FLOWSHEET_KEY
:canonical: idaes_fi.structfs.common.RESULT_FLOWSHEET_KEY
:value: >
   '__fi'

```{autodoc2-docstring} idaes_fi.structfs.common.RESULT_FLOWSHEET_KEY
```

````

`````{py:class} ActionNames(*args, **kwds)
:canonical: idaes_fi.structfs.common.ActionNames

Bases: {py:obj}`enum.Enum`

````{py:attribute} SOLVER_OUTPUT
:canonical: idaes_fi.structfs.common.ActionNames.SOLVER_OUTPUT
:value: >
   'solver_output'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.SOLVER_OUTPUT
```

````

````{py:attribute} SOLVER_RESULTS
:canonical: idaes_fi.structfs.common.ActionNames.SOLVER_RESULTS
:value: >
   'solver_results'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.SOLVER_RESULTS
```

````

````{py:attribute} DIAGNOSTICS
:canonical: idaes_fi.structfs.common.ActionNames.DIAGNOSTICS
:value: >
   'diagnostics'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.DIAGNOSTICS
```

````

````{py:attribute} MODEL_VARIABLES
:canonical: idaes_fi.structfs.common.ActionNames.MODEL_VARIABLES
:value: >
   'model_variables'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.MODEL_VARIABLES
```

````

````{py:attribute} MERMAID_DIAGRAM
:canonical: idaes_fi.structfs.common.ActionNames.MERMAID_DIAGRAM
:value: >
   'mermaid_diagram'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.MERMAID_DIAGRAM
```

````

````{py:attribute} STREAM_TABLE
:canonical: idaes_fi.structfs.common.ActionNames.STREAM_TABLE
:value: >
   'stream_table'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.STREAM_TABLE
```

````

````{py:attribute} DOF
:canonical: idaes_fi.structfs.common.ActionNames.DOF
:value: >
   'degrees_of_freedom'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.DOF
```

````

````{py:attribute} TIMINGS
:canonical: idaes_fi.structfs.common.ActionNames.TIMINGS
:value: >
   'timings'

```{autodoc2-docstring} idaes_fi.structfs.common.ActionNames.TIMINGS
```

````

`````

`````{py:class} Steps
:canonical: idaes_fi.structfs.common.Steps

```{autodoc2-docstring} idaes_fi.structfs.common.Steps
```

````{py:attribute} build
:canonical: idaes_fi.structfs.common.Steps.build
:value: >
   'build'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.build
```

````

````{py:attribute} set_solver
:canonical: idaes_fi.structfs.common.Steps.set_solver
:value: >
   'set_solver'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.set_solver
```

````

````{py:attribute} initialize
:canonical: idaes_fi.structfs.common.Steps.initialize
:value: >
   'initialize'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.initialize
```

````

````{py:attribute} set_operating_conditions
:canonical: idaes_fi.structfs.common.Steps.set_operating_conditions
:value: >
   'set_operating_conditions'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.set_operating_conditions
```

````

````{py:attribute} set_scaling
:canonical: idaes_fi.structfs.common.Steps.set_scaling
:value: >
   'set_scaling'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.set_scaling
```

````

````{py:attribute} solve_initial
:canonical: idaes_fi.structfs.common.Steps.solve_initial
:value: >
   'solve_initial'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.solve_initial
```

````

````{py:attribute} set_autoscaling
:canonical: idaes_fi.structfs.common.Steps.set_autoscaling
:value: >
   'set_autoscaling'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.set_autoscaling
```

````

````{py:attribute} add_costing
:canonical: idaes_fi.structfs.common.Steps.add_costing
:value: >
   'add_costing'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.add_costing
```

````

````{py:attribute} initialize_costing
:canonical: idaes_fi.structfs.common.Steps.initialize_costing
:value: >
   'initialize_costing'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.initialize_costing
```

````

````{py:attribute} setup_optimization
:canonical: idaes_fi.structfs.common.Steps.setup_optimization
:value: >
   'setup_optimization'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.setup_optimization
```

````

````{py:attribute} solve_optimization
:canonical: idaes_fi.structfs.common.Steps.solve_optimization
:value: >
   'solve_optimization'

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.solve_optimization
```

````

````{py:attribute} index
:canonical: idaes_fi.structfs.common.Steps.index
:value: >
   ()

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.index
```

````

````{py:method} __len__()
:canonical: idaes_fi.structfs.common.Steps.__len__
:classmethod:

```{autodoc2-docstring} idaes_fi.structfs.common.Steps.__len__
```

````

`````

````{py:function} load_module(module_or_path: str | pathlib.Path)
:canonical: idaes_fi.structfs.common.load_module

```{autodoc2-docstring} idaes_fi.structfs.common.load_module
```
````

````{py:function} find_flowsheet_objects(a_module) -> dict[str, object]
:canonical: idaes_fi.structfs.common.find_flowsheet_objects

```{autodoc2-docstring} idaes_fi.structfs.common.find_flowsheet_objects
```
````

````{py:exception} FlowsheetLoadError()
:canonical: idaes_fi.structfs.common.FlowsheetLoadError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} idaes_fi.structfs.common.FlowsheetLoadError
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.common.FlowsheetLoadError.__init__
```

````

````{py:function} _get_steps_for_flowsheet(fs: str, fs_attr: str | None) -> list[str]
:canonical: idaes_fi.structfs.common._get_steps_for_flowsheet

```{autodoc2-docstring} idaes_fi.structfs.common._get_steps_for_flowsheet
```
````

````{py:function} main(*cmdline)
:canonical: idaes_fi.structfs.common.main

```{autodoc2-docstring} idaes_fi.structfs.common.main
```
````

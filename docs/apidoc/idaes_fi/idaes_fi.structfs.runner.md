# {py:mod}`idaes_fi.structfs.runner`

```{py:module} idaes_fi.structfs.runner
```

```{autodoc2-docstring} idaes_fi.structfs.runner
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Step <idaes_fi.structfs.runner.Step>`
  - ```{autodoc2-docstring} idaes_fi.structfs.runner.Step
    :summary:
    ```
* - {py:obj}`Runner <idaes_fi.structfs.runner.Runner>`
  - ```{autodoc2-docstring} idaes_fi.structfs.runner.Runner
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__author__ <idaes_fi.structfs.runner.__author__>`
  - ```{autodoc2-docstring} idaes_fi.structfs.runner.__author__
    :summary:
    ```
* - {py:obj}`_log <idaes_fi.structfs.runner._log>`
  - ```{autodoc2-docstring} idaes_fi.structfs.runner._log
    :summary:
    ```
* - {py:obj}`ActionType <idaes_fi.structfs.runner.ActionType>`
  - ```{autodoc2-docstring} idaes_fi.structfs.runner.ActionType
    :summary:
    ```
````

### API

````{py:data} __author__
:canonical: idaes_fi.structfs.runner.__author__
:value: >
   'Dan Gunter (LBNL)'

```{autodoc2-docstring} idaes_fi.structfs.runner.__author__
```

````

````{py:data} _log
:canonical: idaes_fi.structfs.runner._log
:value: >
   'getLogger(...)'

```{autodoc2-docstring} idaes_fi.structfs.runner._log
```

````

`````{py:class} Step(name: str, func: typing.Callable)
:canonical: idaes_fi.structfs.runner.Step

```{autodoc2-docstring} idaes_fi.structfs.runner.Step
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.runner.Step.__init__
```

````{py:attribute} SEP
:canonical: idaes_fi.structfs.runner.Step.SEP
:value: >
   '::'

```{autodoc2-docstring} idaes_fi.structfs.runner.Step.SEP
```

````

````{py:method} add_substep(name: str, func: typing.Callable)
:canonical: idaes_fi.structfs.runner.Step.add_substep

```{autodoc2-docstring} idaes_fi.structfs.runner.Step.add_substep
```

````

`````

````{py:data} ActionType
:canonical: idaes_fi.structfs.runner.ActionType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} idaes_fi.structfs.runner.ActionType
```

````

`````{py:class} Runner(steps: typing.Sequence[str], report_db: idaes_fi.structfs.reportdb.ReportDB = None)
:canonical: idaes_fi.structfs.runner.Runner

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.__init__
```

````{py:attribute} STEP_ANY
:canonical: idaes_fi.structfs.runner.Runner.STEP_ANY
:value: >
   '-'

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.STEP_ANY
```

````

````{py:property} failed
:canonical: idaes_fi.structfs.runner.Runner.failed
:type: bool

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.failed
```

````

````{py:property} failed_actions
:canonical: idaes_fi.structfs.runner.Runner.failed_actions
:type: dict[str, str]

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.failed_actions
```

````

````{py:method} get_defined_steps() -> list[str]
:canonical: idaes_fi.structfs.runner.Runner.get_defined_steps

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.get_defined_steps
```

````

````{py:method} get_report_db() -> idaes_fi.structfs.reportdb.ReportDB
:canonical: idaes_fi.structfs.runner.Runner.get_report_db

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.get_report_db
```

````

````{py:method} set_report_db(db: typing.Optional[idaes_fi.structfs.reportdb.ReportDB] = None, dbfile: typing.Optional[pathlib.Path | str] = None, create: bool = True) -> idaes_fi.structfs.reportdb.ReportDB
:canonical: idaes_fi.structfs.runner.Runner.set_report_db

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.set_report_db
```

````

````{py:method} get_default_report_db(create=False) -> idaes_fi.structfs.reportdb.ReportDB
:canonical: idaes_fi.structfs.runner.Runner.get_default_report_db
:classmethod:

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.get_default_report_db
```

````

````{py:method} __getitem__(key)
:canonical: idaes_fi.structfs.runner.Runner.__getitem__

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.__getitem__
```

````

````{py:method} __getattr__(key)
:canonical: idaes_fi.structfs.runner.Runner.__getattr__

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.__getattr__
```

````

````{py:method} add_step(name: str, func: typing.Callable)
:canonical: idaes_fi.structfs.runner.Runner.add_step

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.add_step
```

````

````{py:method} add_substep(base_name, name, func)
:canonical: idaes_fi.structfs.runner.Runner.add_substep

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.add_substep
```

````

````{py:method} run_step(name)
:canonical: idaes_fi.structfs.runner.Runner.run_step

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.run_step
```

````

````{py:method} run_steps(first: str = '', last: str = '', after: str = '', before: str = '', closest_step=False, save_report=True)
:canonical: idaes_fi.structfs.runner.Runner.run_steps

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.run_steps
```

````

````{py:method} _run_steps(first: str, last: str, endpoints: tuple[bool, bool], closest: bool)
:canonical: idaes_fi.structfs.runner.Runner._run_steps

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._run_steps
```

````

````{py:method} _save_report()
:canonical: idaes_fi.structfs.runner.Runner._save_report

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._save_report
```

````

````{py:method} set_report_target(**target_kw)
:canonical: idaes_fi.structfs.runner.Runner.set_report_target

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.set_report_target
```

````

````{py:method} get_report_target() -> dict
:canonical: idaes_fi.structfs.runner.Runner.get_report_target

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.get_report_target
```

````

````{py:method} reset()
:canonical: idaes_fi.structfs.runner.Runner.reset

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.reset
```

````

````{py:method} list_steps(all_steps=False) -> list[str]
:canonical: idaes_fi.structfs.runner.Runner.list_steps

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.list_steps
```

````

````{py:method} add_action(name: str, action_class: type, *args, **kwargs) -> object
:canonical: idaes_fi.structfs.runner.Runner.add_action

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.add_action
```

````

````{py:method} get_action(name: str) -> idaes_fi.structfs.runner.ActionType
:canonical: idaes_fi.structfs.runner.Runner.get_action

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.get_action
```

````

````{py:method} remove_action(name: str)
:canonical: idaes_fi.structfs.runner.Runner.remove_action

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.remove_action
```

````

````{py:method} _find_step(reverse=False)
:canonical: idaes_fi.structfs.runner.Runner._find_step

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._find_step
```

````

````{py:method} normalize_name(s: typing.Optional[str]) -> str
:canonical: idaes_fi.structfs.runner.Runner.normalize_name
:classmethod:

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.normalize_name
```

````

````{py:method} step_begin(name: str)
:canonical: idaes_fi.structfs.runner.Runner.step_begin

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.step_begin
```

````

````{py:method} _substep_begin(base: str, name: str)
:canonical: idaes_fi.structfs.runner.Runner._substep_begin

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._substep_begin
```

````

````{py:method} step_end(name: str)
:canonical: idaes_fi.structfs.runner.Runner.step_end

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.step_end
```

````

````{py:method} _substep_end(base: str, name: str)
:canonical: idaes_fi.structfs.runner.Runner._substep_end

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._substep_end
```

````

````{py:method} _step_failed(name: str, err: Exception)
:canonical: idaes_fi.structfs.runner.Runner._step_failed

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner._step_failed
```

````

````{py:method} substep(base: str, name: str)
:canonical: idaes_fi.structfs.runner.Runner.substep

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.substep
```

````

````{py:method} report() -> dict[str, dict]
:canonical: idaes_fi.structfs.runner.Runner.report

```{autodoc2-docstring} idaes_fi.structfs.runner.Runner.report
```

````

`````

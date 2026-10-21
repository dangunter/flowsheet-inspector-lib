# {py:mod}`idaes_fi.structfs.action_base`

```{py:module} idaes_fi.structfs.action_base
```

```{autodoc2-docstring} idaes_fi.structfs.action_base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Action <idaes_fi.structfs.action_base.Action>`
  - ```{autodoc2-docstring} idaes_fi.structfs.action_base.Action
    :summary:
    ```
````

### API

`````{py:class} Action(runner: idaes_fi.structfs.runner.Runner, log: typing.Optional[logging.Logger] = None)
:canonical: idaes_fi.structfs.action_base.Action

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.__init__
```

````{py:method} _get_logger()
:canonical: idaes_fi.structfs.action_base.Action._get_logger

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action._get_logger
```

````

````{py:method} before_step(step_name: str)
:canonical: idaes_fi.structfs.action_base.Action.before_step

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.before_step
```

````

````{py:method} before_substep(step_name: str, substep_name: str)
:canonical: idaes_fi.structfs.action_base.Action.before_substep

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.before_substep
```

````

````{py:method} after_step(step_name: str)
:canonical: idaes_fi.structfs.action_base.Action.after_step

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.after_step
```

````

````{py:method} after_substep(step_name: str, substep_name: str)
:canonical: idaes_fi.structfs.action_base.Action.after_substep

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.after_substep
```

````

````{py:method} step_failed(step_name: str, err: Exception)
:canonical: idaes_fi.structfs.action_base.Action.step_failed

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.step_failed
```

````

````{py:method} before_run()
:canonical: idaes_fi.structfs.action_base.Action.before_run

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.before_run
```

````

````{py:method} after_run()
:canonical: idaes_fi.structfs.action_base.Action.after_run

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.after_run
```

````

````{py:method} report() -> pydantic.BaseModel | dict
:canonical: idaes_fi.structfs.action_base.Action.report
:abstractmethod:

```{autodoc2-docstring} idaes_fi.structfs.action_base.Action.report
```

````

`````

# {py:mod}`idaes_fi.compute_diagnostics`

```{py:module} idaes_fi.compute_diagnostics
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ComponentListData <idaes_fi.compute_diagnostics.ComponentListData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData
    :summary:
    ```
* - {py:obj}`VariableListData <idaes_fi.compute_diagnostics.VariableListData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableListData
    :summary:
    ```
* - {py:obj}`ComponentList <idaes_fi.compute_diagnostics.ComponentList>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentList
    :summary:
    ```
* - {py:obj}`VCSet <idaes_fi.compute_diagnostics.VCSet>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet
    :summary:
    ```
* - {py:obj}`EvalErrorData <idaes_fi.compute_diagnostics.EvalErrorData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.EvalErrorData
    :summary:
    ```
* - {py:obj}`StructuralWarningsData <idaes_fi.compute_diagnostics.StructuralWarningsData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData
    :summary:
    ```
* - {py:obj}`StructuralCautionsData <idaes_fi.compute_diagnostics.StructuralCautionsData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData
    :summary:
    ```
* - {py:obj}`StructuralIssuesData <idaes_fi.compute_diagnostics.StructuralIssuesData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralIssuesData
    :summary:
    ```
* - {py:obj}`NumericalWarningsData <idaes_fi.compute_diagnostics.NumericalWarningsData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData
    :summary:
    ```
* - {py:obj}`NumericalIssuesData <idaes_fi.compute_diagnostics.NumericalIssuesData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalIssuesData
    :summary:
    ```
* - {py:obj}`VariableCondition <idaes_fi.compute_diagnostics.VariableCondition>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition
    :summary:
    ```
* - {py:obj}`ConstraintCondition <idaes_fi.compute_diagnostics.ConstraintCondition>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition
    :summary:
    ```
* - {py:obj}`DiagnosticsData <idaes_fi.compute_diagnostics.DiagnosticsData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_block_list_names <idaes_fi.compute_diagnostics._block_list_names>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics._block_list_names
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__author__ <idaes_fi.compute_diagnostics.__author__>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.__author__
    :summary:
    ```
* - {py:obj}`ConstraintListData <idaes_fi.compute_diagnostics.ConstraintListData>`
  - ```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintListData
    :summary:
    ```
````

### API

````{py:data} __author__
:canonical: idaes_fi.compute_diagnostics.__author__
:value: >
   'Dan Gunter (LBNL)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.__author__
```

````

````{py:function} _block_list_names(blocks) -> list[str]
:canonical: idaes_fi.compute_diagnostics._block_list_names

```{autodoc2-docstring} idaes_fi.compute_diagnostics._block_list_names
```
````

`````{py:class} ComponentListData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.ComponentListData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.__init__
```

````{py:property} empty
:canonical: idaes_fi.compute_diagnostics.ComponentListData.empty
:type: bool

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.empty
```

````

````{py:attribute} tag
:canonical: idaes_fi.compute_diagnostics.ComponentListData.tag
:type: str
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.tag
```

````

````{py:attribute} description
:canonical: idaes_fi.compute_diagnostics.ComponentListData.description
:type: str
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.description
```

````

````{py:attribute} names
:canonical: idaes_fi.compute_diagnostics.ComponentListData.names
:type: list[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.names
```

````

````{py:attribute} values
:canonical: idaes_fi.compute_diagnostics.ComponentListData.values
:type: list[float | None]
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.values
```

````

````{py:attribute} value_format
:canonical: idaes_fi.compute_diagnostics.ComponentListData.value_format
:type: str
:value: >
   '.6E'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.value_format
```

````

````{py:attribute} bounds
:canonical: idaes_fi.compute_diagnostics.ComponentListData.bounds
:type: dict
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.bounds
```

````

````{py:attribute} bounds_desc
:canonical: idaes_fi.compute_diagnostics.ComponentListData.bounds_desc
:type: str | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.bounds_desc
```

````

````{py:attribute} details
:canonical: idaes_fi.compute_diagnostics.ComponentListData.details
:type: list[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentListData.details
```

````

`````

`````{py:class} VariableListData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.VariableListData

Bases: {py:obj}`idaes_fi.compute_diagnostics.ComponentListData`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableListData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableListData.__init__
```

````{py:attribute} units
:canonical: idaes_fi.compute_diagnostics.VariableListData.units
:type: list[str]
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableListData.units
```

````

````{py:attribute} ranges
:canonical: idaes_fi.compute_diagnostics.VariableListData.ranges
:type: list[tuple[float | None, float | None]]
:value: >
   'Field(...)'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableListData.ranges
```

````

`````

````{py:data} ConstraintListData
:canonical: idaes_fi.compute_diagnostics.ConstraintListData
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintListData
```

````

`````{py:class} ComponentList(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.ComponentList

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentList
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentList.__init__
```

````{py:attribute} components
:canonical: idaes_fi.compute_diagnostics.ComponentList.components
:type: list[idaes_fi.compute_diagnostics.ComponentListData]
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ComponentList.components
```

````

`````

`````{py:class} VCSet(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.VCSet

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet.__init__
```

````{py:attribute} variables
:canonical: idaes_fi.compute_diagnostics.VCSet.variables
:type: list[str]
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet.variables
```

````

````{py:attribute} constraints
:canonical: idaes_fi.compute_diagnostics.VCSet.constraints
:type: list[str]
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet.constraints
```

````

````{py:method} from_blocks(var_blocks, const_blocks) -> idaes_fi.compute_diagnostics.VCSet
:canonical: idaes_fi.compute_diagnostics.VCSet.from_blocks
:classmethod:

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VCSet.from_blocks
```

````

`````

`````{py:class} EvalErrorData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.EvalErrorData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.EvalErrorData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.EvalErrorData.__init__
```

````{py:attribute} component_name
:canonical: idaes_fi.compute_diagnostics.EvalErrorData.component_name
:type: str
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.EvalErrorData.component_name
```

````

````{py:attribute} message
:canonical: idaes_fi.compute_diagnostics.EvalErrorData.message
:type: str
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.EvalErrorData.message
```

````

`````

`````{py:class} StructuralWarningsData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.__init__
```

````{py:attribute} dof
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData.dof
:type: int | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.dof
```

````

````{py:attribute} inconsistent_units
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData.inconsistent_units
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.inconsistent_units
```

````

````{py:attribute} underconstrained_set
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData.underconstrained_set
:type: idaes_fi.compute_diagnostics.VCSet | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.underconstrained_set
```

````

````{py:attribute} overconstrained_set
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData.overconstrained_set
:type: idaes_fi.compute_diagnostics.VCSet | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.overconstrained_set
```

````

````{py:attribute} evaluation_errors
:canonical: idaes_fi.compute_diagnostics.StructuralWarningsData.evaluation_errors
:type: list[idaes_fi.compute_diagnostics.EvalErrorData] | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralWarningsData.evaluation_errors
```

````

`````

`````{py:class} StructuralCautionsData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.StructuralCautionsData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData.__init__
```

````{py:attribute} zero_vars
:canonical: idaes_fi.compute_diagnostics.StructuralCautionsData.zero_vars
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData.zero_vars
```

````

````{py:attribute} unused_vars_free
:canonical: idaes_fi.compute_diagnostics.StructuralCautionsData.unused_vars_free
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData.unused_vars_free
```

````

````{py:attribute} unused_vars_fixed
:canonical: idaes_fi.compute_diagnostics.StructuralCautionsData.unused_vars_fixed
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralCautionsData.unused_vars_fixed
```

````

`````

`````{py:class} StructuralIssuesData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.StructuralIssuesData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralIssuesData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralIssuesData.__init__
```

````{py:attribute} warnings
:canonical: idaes_fi.compute_diagnostics.StructuralIssuesData.warnings
:type: idaes_fi.compute_diagnostics.StructuralWarningsData
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralIssuesData.warnings
```

````

````{py:attribute} cautions
:canonical: idaes_fi.compute_diagnostics.StructuralIssuesData.cautions
:type: idaes_fi.compute_diagnostics.StructuralCautionsData
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.StructuralIssuesData.cautions
```

````

`````

`````{py:class} NumericalWarningsData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.NumericalWarningsData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData.__init__
```

````{py:attribute} constraints_with_large_residuals
:canonical: idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_with_large_residuals
:type: idaes_fi.compute_diagnostics.ComponentListData | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_with_large_residuals
```

````

````{py:attribute} constraints_with_extreme_jacobians
:canonical: idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_with_extreme_jacobians
:type: idaes_fi.compute_diagnostics.ComponentListData | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_with_extreme_jacobians
```

````

````{py:attribute} constraints_parallel
:canonical: idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_parallel
:type: idaes_fi.compute_diagnostics.ComponentList | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData.constraints_parallel
```

````

````{py:attribute} variables_parallel
:canonical: idaes_fi.compute_diagnostics.NumericalWarningsData.variables_parallel
:type: idaes_fi.compute_diagnostics.ComponentList | None
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalWarningsData.variables_parallel
```

````

`````

`````{py:class} NumericalIssuesData(/, **data: typing.Any)
:canonical: idaes_fi.compute_diagnostics.NumericalIssuesData

Bases: {py:obj}`pydantic.BaseModel`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalIssuesData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalIssuesData.__init__
```

````{py:attribute} warnings
:canonical: idaes_fi.compute_diagnostics.NumericalIssuesData.warnings
:type: idaes_fi.compute_diagnostics.NumericalWarningsData
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.NumericalIssuesData.warnings
```

````

`````

`````{py:class} VariableCondition()
:canonical: idaes_fi.compute_diagnostics.VariableCondition

Bases: {py:obj}`str`, {py:obj}`enum.Enum`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.__init__
```

````{py:attribute} external
:canonical: idaes_fi.compute_diagnostics.VariableCondition.external
:value: >
   'are external variables that appear in constraints'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.external
```

````

````{py:attribute} unused
:canonical: idaes_fi.compute_diagnostics.VariableCondition.unused
:value: >
   'do not appear in any activated constraints'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.unused
```

````

````{py:attribute} fixed_to_zero
:canonical: idaes_fi.compute_diagnostics.VariableCondition.fixed_to_zero
:value: >
   'are fixed to zero'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.fixed_to_zero
```

````

````{py:attribute} at_or_outside_bounds
:canonical: idaes_fi.compute_diagnostics.VariableCondition.at_or_outside_bounds
:value: >
   'have values that fall at or outside their bounds'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.at_or_outside_bounds
```

````

````{py:attribute} with_none_value
:canonical: idaes_fi.compute_diagnostics.VariableCondition.with_none_value
:value: >
   'have a value of none'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.with_none_value
```

````

````{py:attribute} value_near_zero
:canonical: idaes_fi.compute_diagnostics.VariableCondition.value_near_zero
:value: >
   'have a value near zero'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.value_near_zero
```

````

````{py:attribute} extreme_values
:canonical: idaes_fi.compute_diagnostics.VariableCondition.extreme_values
:value: >
   'have extreme values'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.extreme_values
```

````

````{py:attribute} near_bounds
:canonical: idaes_fi.compute_diagnostics.VariableCondition.near_bounds
:value: >
   'have values close to their bounds'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.near_bounds
```

````

````{py:attribute} extreme_jacobians
:canonical: idaes_fi.compute_diagnostics.VariableCondition.extreme_jacobians
:value: >
   'corresponding to Jacobian columns with extreme norms'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.VariableCondition.extreme_jacobians
```

````

`````

`````{py:class} ConstraintCondition()
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition

Bases: {py:obj}`str`, {py:obj}`enum.Enum`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.__init__
```

````{py:attribute} large_residuals
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition.large_residuals
:value: >
   'have residuals greater than specified tolerance'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.large_residuals
```

````

````{py:attribute} no_free_variables
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition.no_free_variables
:value: >
   'do not have any free variables'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.no_free_variables
```

````

````{py:attribute} canceling_terms
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition.canceling_terms
:value: >
   'have additive terms which potentially cancel each other'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.canceling_terms
```

````

````{py:attribute} mismatched_terms
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition.mismatched_terms
:value: >
   'have additive terms of different magnitude'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.mismatched_terms
```

````

````{py:attribute} extreme_jacobians
:canonical: idaes_fi.compute_diagnostics.ConstraintCondition.extreme_jacobians
:value: >
   'corresponding to Jacobian rows with extreme L2 norms'

```{autodoc2-docstring} idaes_fi.compute_diagnostics.ConstraintCondition.extreme_jacobians
```

````

`````

````{py:exception} DiagnosticsError()
:canonical: idaes_fi.compute_diagnostics.DiagnosticsError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsError
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsError.__init__
```

````

`````{py:class} DiagnosticsData(toolbox: idaes.core.util.diagnostics_tools.DiagnosticsToolbox = None, model=None)
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.__init__
```

````{py:attribute} VC
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.VC
:value: >
   None

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.VC
```

````

````{py:method} _collect_potential_eval_errors(toolbox: idaes.core.util.diagnostics_tools.DiagnosticsToolbox) -> list[str]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._collect_potential_eval_errors
:staticmethod:

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._collect_potential_eval_errors
```

````

````{py:method} _verify_active_variables_initialized(toolbox: idaes.core.util.diagnostics_tools.DiagnosticsToolbox) -> None
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._verify_active_variables_initialized
:staticmethod:

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._verify_active_variables_initialized
```

````

````{py:method} _collect_constraint_mismatches(toolbox: idaes.core.util.diagnostics_tools.DiagnosticsToolbox) -> tuple[list[str], list[str], list[str]]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._collect_constraint_mismatches
:staticmethod:

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._collect_constraint_mismatches
```

````

````{py:method} all_as_dict() -> dict[str, dict]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.all_as_dict

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.all_as_dict
```

````

````{py:method} all_as_json(stream=None, **kwargs) -> str | None
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.all_as_json

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.all_as_json
```

````

````{py:method} all_as_obj() -> dict[str, pydantic.BaseModel]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.all_as_obj

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.all_as_obj
```

````

````{py:method} variables(conditions: list[idaes_fi.compute_diagnostics.VariableCondition] | None = None) -> idaes_fi.compute_diagnostics.ComponentList | list[dict]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.variables

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.variables
```

````

````{py:method} constraints(conditions: list[idaes_fi.compute_diagnostics.ConstraintCondition] | None = None) -> idaes_fi.compute_diagnostics.ComponentList | list[dict]
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.constraints

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.constraints
```

````

````{py:method} _get_components_for_conditions(conditions, cond_enum, getter)
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._get_components_for_conditions

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._get_components_for_conditions
```

````

````{py:method} structural_issues(evaluation_errors=True, unit_consistency=True) -> idaes_fi.compute_diagnostics.StructuralIssuesData
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.structural_issues

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.structural_issues
```

````

````{py:method} numerical_issues(parallel_components=True) -> idaes_fi.compute_diagnostics.ComponentList
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData.numerical_issues

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData.numerical_issues
```

````

````{py:method} _get_variables_for_condition(cond: idaes_fi.compute_diagnostics.VariableCondition) -> idaes_fi.compute_diagnostics.ComponentListData
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._get_variables_for_condition

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._get_variables_for_condition
```

````

````{py:method} _get_constraints_for_condition(cond: idaes_fi.compute_diagnostics.ConstraintCondition) -> idaes_fi.compute_diagnostics.ComponentListData
:canonical: idaes_fi.compute_diagnostics.DiagnosticsData._get_constraints_for_condition

```{autodoc2-docstring} idaes_fi.compute_diagnostics.DiagnosticsData._get_constraints_for_condition
```

````

`````

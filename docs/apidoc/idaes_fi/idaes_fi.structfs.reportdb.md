# {py:mod}`idaes_fi.structfs.reportdb`

```{py:module} idaes_fi.structfs.reportdb
```

```{autodoc2-docstring} idaes_fi.structfs.reportdb
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ReportDB <idaes_fi.structfs.reportdb.ReportDB>`
  - ```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__author__ <idaes_fi.structfs.reportdb.__author__>`
  - ```{autodoc2-docstring} idaes_fi.structfs.reportdb.__author__
    :summary:
    ```
* - {py:obj}`_log <idaes_fi.structfs.reportdb._log>`
  - ```{autodoc2-docstring} idaes_fi.structfs.reportdb._log
    :summary:
    ```
````

### API

````{py:data} __author__
:canonical: idaes_fi.structfs.reportdb.__author__
:value: >
   'Dan Gunter (LBNL)'

```{autodoc2-docstring} idaes_fi.structfs.reportdb.__author__
```

````

````{py:data} _log
:canonical: idaes_fi.structfs.reportdb._log
:value: >
   'getLogger(...)'

```{autodoc2-docstring} idaes_fi.structfs.reportdb._log
```

````

`````{py:class} ReportDB(filename: str, **target_kw)
:canonical: idaes_fi.structfs.reportdb.ReportDB

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB
```

```{rubric} Initialization
```

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.__init__
```

````{py:attribute} TABLE
:canonical: idaes_fi.structfs.reportdb.ReportDB.TABLE
:value: >
   'reports'

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.TABLE
```

````

````{py:attribute} TARGET_COLUMNS
:canonical: idaes_fi.structfs.reportdb.ReportDB.TARGET_COLUMNS
:value: >
   (('name', 'TEXT'), ('module', 'TEXT'), ('filedir', 'TEXT'), ('filename', 'TEXT'), ('hash', 'TEXT'))

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.TARGET_COLUMNS
```

````

````{py:attribute} COLUMNS
:canonical: idaes_fi.structfs.reportdb.ReportDB.COLUMNS
:value: >
   'tuple(...)'

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.COLUMNS
```

````

````{py:property} filename
:canonical: idaes_fi.structfs.reportdb.ReportDB.filename
:type: str

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.filename
```

````

````{py:method} set_target(**kw)
:canonical: idaes_fi.structfs.reportdb.ReportDB.set_target

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.set_target
```

````

````{py:method} get_target() -> dict
:canonical: idaes_fi.structfs.reportdb.ReportDB.get_target

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.get_target
```

````

````{py:method} _connect()
:canonical: idaes_fi.structfs.reportdb.ReportDB._connect

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB._connect
```

````

````{py:method} create(drop=False)
:canonical: idaes_fi.structfs.reportdb.ReportDB.create

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.create
```

````

````{py:method} _all_columns(typed=False, exclude=None)
:canonical: idaes_fi.structfs.reportdb.ReportDB._all_columns

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB._all_columns
```

````

````{py:method} add_report(data: str | dict, tags: str = '', run_status: bool = False, run_exc: str = '', solver_status: str = 'NA', **target_kw)
:canonical: idaes_fi.structfs.reportdb.ReportDB.add_report

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.add_report
```

````

````{py:method} get_metadata(tags: str = '', **target_kw)
:canonical: idaes_fi.structfs.reportdb.ReportDB.get_metadata

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.get_metadata
```

````

````{py:method} get_report(index) -> str
:canonical: idaes_fi.structfs.reportdb.ReportDB.get_report

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.get_report
```

````

````{py:method} get_last_meta(**kwargs) -> dict | None
:canonical: idaes_fi.structfs.reportdb.ReportDB.get_last_meta

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.get_last_meta
```

````

````{py:method} get_last_report(**kwargs) -> dict | None
:canonical: idaes_fi.structfs.reportdb.ReportDB.get_last_report

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB.get_last_report
```

````

````{py:method} _where(fltr, tags=None)
:canonical: idaes_fi.structfs.reportdb.ReportDB._where

```{autodoc2-docstring} idaes_fi.structfs.reportdb.ReportDB._where
```

````

`````

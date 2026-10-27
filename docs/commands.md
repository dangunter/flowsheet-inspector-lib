# Command-line interface

The package provides the `ifi` command through the `idaes_fi.commands:main`
entry point. Use `ifi --help` to see the top-level command list.

* Root command: `ifi [options]`
    - Options:
        - `--json/-J`. Where appropriate, show JSON output instead of
          plain text output. Useful for interfacing with scripts and other
          automated processes.
* Database commands: `ifi db <subcommand> [options]`
    - `ifi db info`: Get database information
        - Examples:
            - `ifi db info`: Show information as readable text
            - `ifi --json db info`: Show information as JSON
            - `ifi db info -f my_db.sqlite`: Use specified database instead
              of default database.
        - Python command: 
        ```{python}
        import json
        from idaes_fi.commands import *
        print(json.dumps(db_info(), cls=PathJSONEncoder))
        ```
    - `ifi db migrate`: Migrate database to newest version




OLD 

## Database commands

`db migrate` migrates the default report database to the latest schema:

```console
ifi db migrate
```

Use a specific database file with `--file` (or `-f`):

```console
ifi db migrate --file path/to/report.sqlite
```

`db info` prints the database filename and schema version:

```console
ifi db info --file path/to/report.sqlite
```

If `--file` is omitted, the configured default report database is used.

## Flowsheet commands

Run a wrapped flowsheet from a Python module:

```console
ifi flowsheet run --module my_flowsheet
```

Run a flowsheet from a Python file instead:

```console
ifi flowsheet run --file path/to/my_flowsheet.py
```

If a module or file defines more than one flowsheet runner, select one with
`--name` (or `-n`):

```console
ifi flowsheet run --module my_flowsheet --name FS2
```

Stop after a named step with `--last-step` (or `-l`):

```console
ifi flowsheet run --module my_flowsheet --last-step initialize
```

Set the flowsheet runner's logging level with `--level` (or `-L`). Level names
are case-insensitive. Supported names are `NOTSET`, `DEBUG`, `INFO`, `WARN`,
`WARNING`, `ERROR`, `FATAL`, and `CRITICAL`; the default is `INFO`.

The `--level` option belongs to the `flowsheet` command, so place it before
the `run` subcommand:

```console
ifi flowsheet --level DEBUG run --module my_flowsheet
```

List the steps defined by a wrapped flowsheet with `flowsheet steps`:

```console
ifi flowsheet steps --module my_flowsheet
ifi flowsheet steps --file path/to/my_flowsheet.py --name FS2
```

Both flowsheet subcommands require either `--module` or `--file`.

## Programmatic use

The command functions can be called directly from Python without constructing
an argument list or invoking a subprocess.

```python
from idaes_fi.commands import db_info, db_migrate, flowsheet_run, flowsheet_steps

# Use the default report database, or pass a database path.
info = db_info("path/to/report.sqlite")
print(info["version"])
db_migrate("path/to/report.sqlite")

# Run or inspect a flowsheet from a module.
flowsheet_run(
    module="my_flowsheet",
    name="FS2",
    last_step="initialize",
)
steps = flowsheet_steps(module="my_flowsheet", name="FS2")
print(steps)
```

For a Python file, use `file` instead of `module`:

```python
from idaes_fi.commands import flowsheet_run

flowsheet_run(file="path/to/my_flowsheet.py", level=20)  # logging.INFO
```

`flowsheet_run()` accepts a numeric logging level, such as the constants in
Python's `logging` module. It runs the selected flowsheet and returns `None`;
`flowsheet_steps()` returns the runner's list of step names; and `db_info()`
returns a dictionary containing `file` and `version`.

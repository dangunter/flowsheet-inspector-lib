# Commands

## Console command-line interface 

The package provides the `ifi` command for console usage
(the mnemonic is **I**DAES **F**lowsheet **I**nspector).
Use `ifi --help` to see the top-level command list.

Global options:
<dl class="args">
<dt>--json/-J</dt>
<dd>Where appropriate, show JSON output instead of plain text output. Useful for interfacing with scripts and other automated processes.</dd>
</dl>

Subcommands:
<dl class="args">
<dt>db</dt><dd>Inspect or modify the database</dd>
<dt>flowsheet</dt><dd>Inspect or run flowsheets</dd>
</dl>

These subcommands have further sub-subcommands.
Use `ifi <subcommand> --help` to see help for each subcommand and
a list of their sub-subcommands and, finally, `ifi <subcommand> <sub-subcommand> --help` to see options for the actual function to execute.
For example: `ifi db migrate --help` will show options for the database
migration function.

## Programmatic usage

Each sub-command available through the `ifi` command can also be found in the `idaes_fi.commands` module, where the name of the function is simply the subcommand and sub-subcommand name separated by an underscore.
For example: `ifi db migrate` &rarr; <tt>idaes_fi.commands.db_migrate()</tt>.

## Python interpreter usage

Finally, to run the commands using the Python interpreter's `-c` option, which avoids having to invoke the `ifi` command through the shell, you can import the module and use the functions directly.

Note that formatting of the output is done by the CLI wrapper, so this may need to be recreated. For example, to print out DB info as JSON you can run: `python -c "import json; from idaes_fi.commands import *; print(json.dumps(db_info(), cls=PathJSONEncoder))"`. The PathJSONEncoder class is defined in the *commands* module in order to handle Python's *pathlib.Path* objects. 
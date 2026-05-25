# stdlib
from enum import StrEnum, auto
from io import IOBase
from pathlib import Path
import sys

# third-party
from jinja2 import Environment, PackageLoader, select_autoescape

# pkg
from .. import actions


class InvalidReportError(Exception):
    pass


class ReportFormat(StrEnum):
    markdown = auto()
    html = auto()
    text = auto()


class TextReport:
    """Use Jinja2 templates to create text reports.

    Basic usage follows 3 steps:

    1. Get the report data, let's call this `rpt`.
    2. Create an instance of this class: `tr = TextReport(rpt)`.
    3. Write the report to an output stream in a chosen format.
        a. `tr.write()` uses default format (text) and stdout
        b. `tr.write(report_format="markdown")` will write markdown to stdout
        c. `tr.write(stream=open("report.html", "w"), report_format="html")
           will write an HTML-format report to a file

    """

    # Filename extensions for report templates, by format
    REPORT_EXT = {
        ReportFormat.markdown: "md",
        ReportFormat.html: "html",
        ReportFormat.text: "txt",
    }

    def __init__(self, data: dict, name="<name>"):
        """Constructor

        Args:
            data: Report data
            name: Flowsheet name, for report title

        Raises:
            InvalidReportError: if report input doesn't have
                                expected top-level keys
        """
        try:
            self._report_kw = {
                "actions": data["actions"],
                "last": data["last_run"],
                "name": name,
            }
        except KeyError as err:
            raise InvalidReportError(err)

        self._jinja_env = Environment(
            loader=PackageLoader("idaes_fi.structfs.tool", "templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def write(
        self,
        stream: IOBase = sys.stdout,
        report_format: ReportFormat = ReportFormat.text,
    ):
        """Write the template to a stream

        Args:
           stream: output stream (default = standard output)
           report_format: Desired report output format
        """
        stream.write(self.render(report_format))

    def render(self, report_format: ReportFormat) -> str:
        """Render template to a string using report data.

        Args:
           report_format: Desired report output format

        Returns:
            Rendered template string
        """
        ext = self.REPORT_EXT[report_format]
        template = self._jinja_env.get_template(f"report.{ext}")
        return template.render(**self._report_kw)

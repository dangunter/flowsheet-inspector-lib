from tempfile import TemporaryDirectory
from pathlib import Path

import pytest

from idaes_fi.structfs.tests.demo_flowsheet_structured import FS
from .. import text_report


@pytest.fixture(scope="module")
def report_data():
    with TemporaryDirectory() as tmpdir:
        tmp_db = Path(tmpdir) / "text_report.db"
        FS.set_report_db(dbfile=tmp_db)
        FS.run_steps()
        yield FS.report()


@pytest.mark.unit
def test_smoke():
    tr = text_report.TextReport({})


@pytest.mark.unit
def test_text(report_data):
    pass

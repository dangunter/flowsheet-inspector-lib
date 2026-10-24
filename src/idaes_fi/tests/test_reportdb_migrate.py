"""
Test ReportDB migration.
"""

import logging

import pytest

from idaes_fi.reportdb import ReportDB
from idaes_fi.reportdb_migrate import MigrationStrategy, MigrationError


@pytest.fixture(scope="module")
def setup_logging():
    from idaes_fi.reportdb_migrate import _log

    print("Setting up logging")
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    _log.addHandler(h)
    _log.setLevel(logging.DEBUG)
    return _log


@pytest.mark.unit
def test_migration_strategy_smoke():
    strategy = MigrationStrategy()


@pytest.mark.unit
def test_migration_strategy_migrate_invalid_file(tmp_path):
    strategy = MigrationStrategy()
    invalid_file = tmp_path / "invalid.db"
    with open(invalid_file, "w") as f:
        f.write("This is not a valid database file.")
    with pytest.raises(MigrationError):
        strategy.migrate(invalid_file)


@pytest.mark.component
def test_migration_strategy_migrate_1_0_to_1_1(tmp_path, setup_logging):
    # Create a dummy 1.0 database file
    old_db_file = tmp_path / "old_report.db"
    old_db = ReportDB(old_db_file)
    old_db.create()
    # add a fake report
    old_db.add_report({"fake": "data"})
    # drop status table to simulate an older version
    with old_db._connect() as conn:
        conn.execute("DROP TABLE IF EXISTS status")

    # Perform migration
    strategy = MigrationStrategy()
    did_something = False
    try:
        did_something = strategy.migrate(old_db_file)
    except MigrationError as e:
        pytest.fail(f"Migration failed: {e}")
    assert did_something, "Migration should have been performed, but wasn't"

    # Verify that status table exists now
    with old_db._connect() as conn:
        rows = list(conn.execute("SELECT * from status"))
    assert len(rows) == 1

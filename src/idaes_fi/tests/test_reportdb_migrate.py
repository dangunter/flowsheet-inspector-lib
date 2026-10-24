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
@pytest.mark.parametrize("reportnum", [0, 1, 3])
def test_migration_strategy_migrate_1_0_to_1_1(tmp_path, setup_logging, reportnum):
    # Create a dummy 1.0 database file
    old_db_file = tmp_path / "old_report.db"
    old_db = ReportDB(old_db_file)
    old_db.create()
    # add a fake report(s)
    for i in range(reportnum):
        old_db.add_report({"fake": "data"})
    # make changes to simulate an older version
    with old_db._connect() as conn:
        # drop status table
        conn.execute(f"DROP TABLE IF EXISTS {ReportDB.STAT_TABLE}")
        # change version to 1.0
        print(f"UPDATE {ReportDB.VERSION_TABLE} SET major = 1, minor = 0")
        conn.execute(f"UPDATE {ReportDB.VERSION_TABLE} SET major = 1, minor = 0")

    # Perform migration
    strategy = MigrationStrategy()
    did_something = False
    try:
        did_something = strategy.migrate(old_db_file)
    except MigrationError as e:
        pytest.fail(f"Migration failed: {e}")
    assert did_something, "Migration should have been performed, but wasn't"

    # Verify that status table exists now (still named old_db)
    with old_db._connect() as conn:
        rows = list(conn.execute("SELECT * from status"))
    assert len(rows) == reportnum


@pytest.mark.component
@pytest.mark.parametrize("ver", [(0, 0), (2, 0), (1, 99)])
def test_migration_strategy_bad_versions(tmp_path, setup_logging, ver):
    # Create a database file with given version
    old_db_file = tmp_path / "old_report.db"
    old_db = ReportDB(old_db_file)
    old_db.create()
    # Set version
    with old_db._connect() as conn:
        # change version
        versions = f"major = {ver[0]}, minor = {ver[1]}"
        conn.execute(f"UPDATE {ReportDB.VERSION_TABLE} SET {versions}")

    # Perform migration
    strategy = MigrationStrategy()
    with pytest.raises(MigrationError):
        did_something = strategy.migrate(old_db_file)
        assert not did_something

import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.models import Stats
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation


@pytest.mark.django_db
def test_update_statistics_storage(stats, mandals, districts, states):
    # Arrange
    mandal_id = 1
    total_confirmed = 10
    total_deaths = 4
    total_recovered = 3
    date = datetime.date(year=2020, month=5, day=28)
    storage = MandalStorageImplementation()

    # Act
    storage.update_statistics(
        date=date,
        mandal_id=mandal_id,
        total_confirmed=total_confirmed,
        total_recovered=total_recovered,
        total_deaths=total_deaths
    )
    stat = Stats.objects.get(mandal_id=mandal_id, date=date)

    # Assert
    assert stat.mandal_id == mandal_id
    assert stat.total_confirmed == total_confirmed
    assert stat.total_recovered == total_recovered
    assert stat.total_deaths == total_deaths
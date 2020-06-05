import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidStatsDetails

@pytest.mark.django_db
def is_valid_total_stats_when_invalid_details_given_raises_error():
    # Arrange
    total_confirmed = 10
    total_deaths = 10
    total_recovered = 1
    storage = MandalStorageImplementation()

    # Act
    with pytest.raises(InvalidStatsDetails):
        storage.is_statistics_valid(total_confirmed=total_confirmed,
            total_deaths=total_deaths, total_recovered=total_recovered)


@pytest.mark.django_db
def is_valid_total_stats():
    # Arrange
    total_confirmed = 10
    total_deaths = 5
    total_recovered = 1
    storage = MandalStorageImplementation()

    # Act
    result = storage.is_statistics_valid(total_confirmed=total_confirmed,
        total_deaths=total_deaths, total_recovered=total_recovered)

    # Assert
    assert result == None
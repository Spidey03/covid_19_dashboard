import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import *

@pytest.mark.django_db
def test_get_statistics(all_states, all_districts, all_mandals, all_stats):
    # Arrange
    import datetime
    storage = MandalStorageImplementation()
    mandal_id = 1
    expected_result = MandalStatistics(
        mandal_id=1,
        mandal_name='Kallur',
        reports=[
            Statistics(
                date=datetime.date(2020, 5, 22),
                total_cases=5,
                total_deaths=1,
                total_recovered_cases=2
            ),
            Statistics(
                date=datetime.date(2020, 5, 23),
                total_cases=6,
                total_deaths=1,
                total_recovered_cases=2
            ),
            Statistics(
                date=datetime.date(2020, 5, 24),
                total_cases=5,
                total_deaths=4,
                total_recovered_cases=2
            )
        ]
    )

    # Act
    result = storage.get_statistics(mandal_id)

    # Assert
    assert result == expected_result


@pytest.mark.django_db
def test_get_statistics_v2(all_states, all_districts, all_mandals, all_stats):
    # Arrange
    import datetime
    storage = MandalStorageImplementation()
    mandal_id = 5
    expected_result = MandalStatistics(
        mandal_id=5,
        mandal_name='Kavali',
        reports=[]
    )

    # Act
    result = storage.get_statistics(mandal_id)

    # Assert
    assert result == expected_result
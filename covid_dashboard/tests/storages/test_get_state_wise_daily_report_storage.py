import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import Report

@pytest.mark.django_db
def test_get_state_wise_daily_report_storage(
        all_states, all_districts, all_mandals, all_stats):
    # Arrange
    storage = StateStorageImplementation()
    expected_result =  [
        Report(
            date=datetime.date(2020, 5, 20),
            total_cases=5,
            total_recovered_cases=5,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 21),
            total_cases=20,
            total_recovered_cases=10,
            total_deaths=0,
            active_cases=10
        ),
        Report(
            date=datetime.date(2020, 5, 22),
            total_cases=16,
            total_recovered_cases=10,
            total_deaths=3,
            active_cases=3
        ),
        Report(
            date=datetime.date(2020, 5, 23),
            total_cases=27,
            total_recovered_cases=8,
            total_deaths=5,
            active_cases=14
        ),
        Report(
            date=datetime.date(2020, 5, 24),
            total_cases=29,
            total_recovered_cases=4,
            total_deaths=19,
            active_cases=6
        )
    ]
    # Act
    result = storage.get_state_wise_daily_cases_report()

    # Assert
    assert result == expected_result



@pytest.mark.django_db
def test_get_state_wise_daily_report_storage_when_no_cases_on_a_day(
        all_states, all_districts, all_mandals, all_stats2):
    # Arrange
    storage = StateStorageImplementation()
    expected_result = [
        Report(
            date=datetime.date(2020, 5, 22),
            total_cases=5,
            total_recovered_cases=2,
            total_deaths=1,
            active_cases=2
        ),
        Report(
            date=datetime.date(2020, 5, 23),
            total_cases=10,
            total_recovered_cases=2,
            total_deaths=3,
            active_cases=5
        ),
        Report(
            date=datetime.date(2020, 5, 24),
            total_cases=12,
            total_recovered_cases=2,
            total_deaths=4,
            active_cases=6
        ),
        Report(
            date=datetime.date(2020, 5, 25),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 26),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 27),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 28),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 29),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        )
    ]
    # Act
    result = storage.get_state_wise_daily_cases_report()

    # Assert
    assert result == expected_result
import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.tests.storages.conftest\
    import *
from covid_dashboard.interactors.storages.dtos import \
    (DistrictReportForADate, StateReportForADate)


@pytest.mark.django_db
def test_get_report_of_a_state_for_a_date(all_states, all_mandals, districts3, all_stats):
    # Arrange
    date = datetime.date(year=2020, month=5, day=20)
    storage = StateStorageImplementation()
    expected_result = StateReportForADate(
        state_name='Andrapradesh',
        districts=[
            DistrictReportForADate(
                district_id=1,
                district_name='Kurnool',
                total_cases=0,
                total_recovered_cases=0,
                total_deaths=0
            ),
            DistrictReportForADate(
                district_id=2,
                district_name='Nellore',
                total_cases=40,
                total_recovered_cases=20,
                total_deaths=0
            ),
            DistrictReportForADate(
                district_id=3,
                district_name='Ananthapuram',
                total_cases=0,
                total_recovered_cases=0,
                total_deaths=0
            )
        ]
        ,
        total_cases=40,
        total_recovered_cases=20,
        total_deaths=0
    )

    # Act
    result = storage.get_report_of_state_for_date(date)

    # Assert
    assert result == expected_result
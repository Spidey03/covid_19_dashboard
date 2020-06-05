import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.tests.storages.conftest\
    import (cumulative_state_report_dto_no_cases,
            cumulative_state_report_dto
           )

@pytest.mark.django_db
def test_get_state_wise_cumulative_report_storage_when_there_are_no_case_in_district(
        mandals, districts, states):
    # Arrange
    till_date = datetime.date(year=1000, month=1, day=1)
    storage = StateStorageImplementation()
    expected_result = cumulative_state_report_dto_no_cases

    # Act
    result = storage.get_state_wise_cumulative_report(till_date=till_date)

    # Assert
    assert result == expected_result


@pytest.mark.django_db
def test_get_state_wise_cumulative_report_storage_when_cases_present(
        mandals, districts, states, stats):
    # Arrange
    till_date = datetime.date(year=2020, month=5, day=28)
    storage = StateStorageImplementation()
    expected_result = cumulative_state_report_dto

    # Act
    result = storage.get_state_wise_cumulative_report(till_date=till_date)

    # Assert
    assert result == expected_result




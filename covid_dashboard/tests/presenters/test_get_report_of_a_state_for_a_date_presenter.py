import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.presenters.conftest\
    import list_district_daily_cumulative
from covid_dashboard.interactors.storages.dtos\
    import (DistrictReportForADate, StateReportForADate)


def test_get_response_for_get_report_of_state_of_a_date():
    # Arrange
    presenter = PresenterImplementation()
    expected_result = {
        'state_name': 'Andrapradesh',
        'districts': [
            {
                'district_id': 1,
                'district_name': 'Kadapa',
                'total_cases': 0,
                'total_recovered_cases': 0,
                'total_deaths': 0
            },
            {
                'district_id': 2,
                'district_name': 'Kurnool',
                'total_cases': 24,
                'total_recovered_cases': 4,
                'total_deaths': 12
            }
        ],
        'state_total_cases': 24,
        'state_total_recovered_cases': 4,
        'state_total_deaths': 12
    }
    report = StateReportForADate(
        state_name='Andrapradesh',
        districts=[
            DistrictReportForADate(
                district_id=1,
                district_name='Kadapa',
                total_cases=0,
                total_recovered_cases=0,
                total_deaths=0
            ),
            DistrictReportForADate(
                district_id=2,
                district_name='Kurnool',
                total_cases=24,
                total_recovered_cases=4,
                total_deaths=12
            )
        ],
        total_cases=24, 
        total_recovered_cases=4,
        total_deaths=12
    )
    # Act
    result = presenter.get_response_for_report_of_state_for_date(report)

    # Assert
    assert result == expected_result
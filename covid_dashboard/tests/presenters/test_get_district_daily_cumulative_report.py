import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.presenters.conftest\
    import list_district_daily_cumulative


def test_get_district_daily_cumulative_report_response_presenter():
    # Arrange
    presenter = PresenterImplementation()
    expected_result = {
        'state_name': 'Andhrapradesh',
        'districts': [
            {
                'district_id': 1,
                'district_name': 'Kurnool',
                'daily_cumulative': [
                    {
                        'date': datetime.date(2020, 5, 26),
                        'total_cases': 40,
                        'total_deaths': 3,
                        'total_recovered_cases': 37,
                        'active_cases': 0
                    }
                ],
            },
            {
                'district_id': 2,
                'district_name': 'Nellore',
                'daily_cumulative': [
                    {
                        'date': datetime.date(2020, 5, 26),
                        'total_cases': 30,
                        'total_deaths': 3,
                        'total_recovered_cases': 27,
                        'active_cases': 0
                    },
                    {
                        'date': datetime.date(2020, 5, 27),
                        'total_cases': 40,
                        'total_deaths': 3,
                        'total_recovered_cases': 37,
                        'active_cases': 0
                    }
                ],
            }
        ],
    }
    

    # Act
    result = presenter.get_district_daily_cumulative_report_response(
        list_district_daily_cumulative)

    # Assert
    assert result == expected_result

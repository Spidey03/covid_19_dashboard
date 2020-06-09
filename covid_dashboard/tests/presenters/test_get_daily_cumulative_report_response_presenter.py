import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import daily_cumulative_report_dto


def test_get_daily_cumulative_report_response_presenter():
    # Arrange
    presenter = PresenterImplementation()
    expected_result = {
        "daily_cumulative":[
            {
                "date": str(datetime.date(year=2020, month=5, day=28)\
                    .strftime('%d-%b-%Y')),
                "total_cases":20,
                "total_deaths":0,
                "total_recovered_cases":20,
                'active_cases':0
            }
        ]
    }
    

    # Act
    result = presenter.get_daily_cumulative_report_response(
        daily_cumulative_report_dto)

    # Assert
    assert result == expected_result

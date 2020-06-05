import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_report_of_a_state_for_a_date_interactor\
    import GetReportOFStateForDate
from covid_dashboard.exceptions.exceptions\
    import InvalidDate
from covid_dashboard.tests.interactors.conftest import *


def test_get_report_of_state_for_date_with_invalid_details():
    # Arrange
    import datetime
    date = datetime.date(year=2035, month=2, day=25)
    storage = create_autospec(StateStorageInterface)
    storage.check_is_date_valid.side_effect = InvalidDate
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_date.side_effect = InvalidDate

    interactor = GetReportOFStateForDate(storage=storage,
        presenter=presenter)

    # Act
    with pytest.raises(InvalidDate):
        interactor.get_report_of_state_for_date(date)

    storage.check_is_date_valid.assert_called_once_with(date)


def test_get_report_of_state_for_date():
    # Arrange
    import datetime
    date = datetime.date(year=2020, month=5, day=26)
    expected_result = {
        "state_name":"Andrapradesh",
        "districts":[
            {
                "district_id":1,
                "district_name":"Kurnool",
                "total_cases":15,
                "total_deaths":0,
                "total_recovered_cases":5
            },
            {
                "district_id":2,
                "district_name":"Kadapa",
                "total_cases":20,
                "total_deaths":0,
                "total_recovered_cases":8
            },
            {
                "district_id":3,
                "district_name":"nellore",
                "total_cases":0,
                "total_deaths":0,
                "total_recovered_cases":0
            }
        ]
        
    }
    
    storage = create_autospec(StateStorageInterface)
    storage.get_report_of_state_for_date.return_value = state_report_for_date
    
    presenter = create_autospec(PresenterInterface)
    presenter.get_response_for_report_of_state_for_date.return_value = \
        expected_result

    interactor = GetReportOFStateForDate(storage=storage,
        presenter=presenter)

    # Act
    result = interactor.get_report_of_state_for_date(date)

    storage.get_report_of_state_for_date.assert_called_once_with(date)
    assert result == expected_result
import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_state_wise_daily_data_interactor\
    import GetStateWiseDailyReport
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from covid_dashboard.tests.interactors.conftest import *


def get_state_wise_daily_report_interactor():
    # Arrange
    state_id = 1
    storage = create_autospec(StateStorageInterface)
    presenter = create_autospec(PresenterInterface)

    expected_result = {
        "state_name":"Andrapradesh",
        "districts":[
            {
                "district_id":1,
                "district_name":"Kurnool",
                "total_cases":"2",
                "total_deaths": 0,
                "total_recovered_cases": 0,
                "active_cases": 2
            }
        ],
        "total_cases":2,
        "total_deaths": 0,
        "total_recovered_cases": 0,
        "active_cases": 2
    }
    interactor = GetStateWiseDailyReport(storage=storage, presenter=presenter)
    storage.get_state_wise_daily_report.return_value = \
        daily_state_report_dto
    presenter.get_response_for_state_wise_daily_report.return_value = \
        expected_result
        
    # Act
    result = interactor.get_state_wise_daily_report()

    # Assert
    storage.get_state_wise_daily_report.assert_called_once_with()
    presenter.get_response_for_state_wise_daily_report.assert_called_once_with(
        daily_state_report_dto)
    assert expected_result == result
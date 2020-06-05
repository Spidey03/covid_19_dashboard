import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_state_wise_daily_report_interactor\
    import GetStateWiseDailyCasesReport
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from covid_dashboard.tests.interactors.conftest import *


def test_get_state_wise_daily_cases_report_interactor():
    # Arrange
    import datetime

    report = StateDailyReport(
            reports = [
                Report(
                    date=datetime.date(year=2020, month=5, day=25),
                    total_cases=3,
                    total_deaths=0,
                    total_recovered_cases=2,
                    active_cases=1
                ),
                Report(
                    date=datetime.date(year=2020, month=5, day=26),
                    total_cases=0,
                    total_deaths=0,
                    total_recovered_cases=0,
                    active_cases=0
                ),
                Report(
                    date=datetime.date(year=2020, month=5, day=27),
                    total_cases=10,
                    total_deaths=0,
                    total_recovered_cases=6,
                    active_cases=4
                )
                
            ]
        )
    expected_result = {
            "daily_cases":[
                {
                    "date":"2020-05-25",
                    "total_cases":3,
                    "total_deaths":0,
                    "total_recovered_cases":2,
                    "active_cases":1
                },
                {
                    "date":"2020-05-26",
                    "total_cases":0,
                    "total_deaths":0,
                    "total_recovered_cases":0,
                    "active_cases":0
                },
                {
                    "date":"2020-05-27",
                    "total_cases":10,
                    "total_deaths":0,
                    "total_recovered_cases":6,
                    "active_cases":4
                }
            ]
        }
    storage = create_autospec(StateStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetStateWiseDailyCasesReport(
        storage=storage, presenter=presenter)
    storage.get_state_wise_daily_cases_report.return_value = report

    presenter.get_response_for_state_wise_daily_cases_report.return_value = \
        expected_result

    # Act
    result = interactor.get_state_wise_daily_cases_report()

    # Assert
    assert result == expected_result
    presenter.get_response_for_state_wise_daily_cases_report\
        .assert_called_once_with(report)
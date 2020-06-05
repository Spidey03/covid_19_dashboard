import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_daily_cumulative_report_interactor\
    import GetDailyCumulativeReport
from covid_dashboard.tests.interactors.conftest import *


def test_get_daily_cumulative_report_interactor():
    # Arrange
    storage = create_autospec(StateStorageInterface)
    storage.get_daily_cumulative_report.return_value = \
        daily_cumulative_report_dto
    
    presenter = create_autospec(PresenterInterface)
    presenter.get_daily_cumulative_report_response.return_value = \
        daily_cumulative_report
    
    interactor = GetDailyCumulativeReport(
        storage=storage, presenter=presenter)

    # Act
    result = interactor.get_daily_cumulative_report()

    # Assert
    storage.get_daily_cumulative_report.assert_called_once()
    presenter.get_daily_cumulative_report_response\
             .assert_called_once_with(daily_cumulative_report_dto)
    assert result == daily_cumulative_report
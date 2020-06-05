import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_state_wise_cumulative_report_interactor\
    import GetStateWiseCumulativeReport
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from covid_dashboard.tests.interactors.conftest import *


def get_state_wise_cumulative_report_interactor():
    # Arrange
    till_date = datetime.now().date()
    expected_result = state_stats_with_metrics
    storage = create_autospec(StateStorageInterface)
    storage.get_state_wise_cumulative_report.return_value = statedto

    presenter = create_autospec(PresenterInterface)
    presenter.get_response_for_state_wise_cumulative_report.return_value = \
        state_stats_with_metrics

    interactor = GetStateWiseCumulativeReport(
        storage=storage, presenter=presenter
    )

    # Act
    result = interactor.get_state_wise_cumulative_report(till_date=till_date)

    # Assert
    assert result == expected_result
    storage.get_state_wise_cumulative_report.assert_called_once_with(till_date)
    presenter.get_response_for_state_wise_cumulative_report\
        .assert_called_once_with(state_dto_with_metrics)
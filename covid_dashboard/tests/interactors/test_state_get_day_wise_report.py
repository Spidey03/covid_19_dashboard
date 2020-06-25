import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.state_get_day_wise_report_interactor \
    import StateGetDaywiseReportInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat


class TestStateGetDayWiseReport:

    def test_when_state_id_invalid_raises_invalid_state_id(self):

        # Arrange
        state_id=1
    
        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDaywiseReportInteractor(storage=storage)

        storage.check_state_id_is_valid.side_effect = InvalidStateId
        presenter.raise_invalid_state_id.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.state_get_day_wise_report_wrapper(state_id=state_id,
                presenter=presenter)

        # Assert
        storage.check_state_id_is_valid.assert_called_once_with(
            state_id=state_id)
        presenter.raise_invalid_state_id.assert_called_once_with(
            state_id=state_id)

    def test_get_day_wise_report(self, state_daily_report_dtos,
            state_day_wise_report_dtos, state_day_wise_report_response):

        # Arrange
        state_id=1
        expected_output = state_day_wise_report_response

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDaywiseReportInteractor(storage=storage)

        storage.check_state_id_is_valid.return_value = None
        storage.state_get_day_wise_report.return_value = \
            state_daily_report_dtos
        storage.get_initial_and_final_dates.return_value = \
            datetime.date(year=2020, month=5, day=2), \
            datetime.date(year=2020, month=5, day=5)
        presenter.resonse_state_day_wise_report.return_value = \
            state_day_wise_report_response

        # Act
        output = interactor.state_get_day_wise_report_wrapper(state_id=state_id,
            presenter=presenter)

        # Assert
        storage.check_state_id_is_valid.assert_called_once_with(
            state_id=state_id)
        storage.state_get_day_wise_report.assert_called_once_with(
            state_id=state_id)
        presenter.resonse_state_day_wise_report.assert_called_once_with(
            day_wise_report_dtos=state_day_wise_report_dtos)
        assert output == expected_output

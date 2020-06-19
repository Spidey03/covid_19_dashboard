import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.state_get_cumulative_report_interactor \
    import StateGetCumulativeReportInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat


class TestStateGetCumulativeReportInteractor:

    def test_when_invalid_state_id_is_given_raise_invalid_state_id_exception(self):

        # Arrange
        state_id = 1
        till_date = datetime.date.today()

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetCumulativeReportInteractor(storage=storage)

        storage.get_state_details.side_effect = InvalidStateId
        presenter.raise_invalid_state_id.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.state_get_cumulative_report_wrapper(state_id=state_id,
                till_date=till_date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)
        presenter.raise_invalid_state_id.assert_called_once_with(
            state_id=state_id)

    def test_when_invalid_date_format_is_given_raise_invalid_date_format_exception(self, state_dto):

        # Arrange
        state_id = 1
        till_date = "25-02-2020"

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetCumulativeReportInteractor(storage=storage)

        storage.get_state_details.return_value = state_dto
        presenter.raise_invalid_date_format.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.state_get_cumulative_report_wrapper(state_id=state_id,
                till_date=till_date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)

    def test_when_valid_details_are_given_returns_response(self, state_dto,
            district_report_dtos, state_cumulative_report_response, district_dtos):

        # Arrange
        state_id = 1
        district_ids = [1, 2]
        till_date = datetime.date.today()
        expected_response = state_cumulative_report_response

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetCumulativeReportInteractor(storage=storage)

        storage.get_state_details.return_value = state_dto
        storage.get_districts_for_state.return_value = district_dtos
        storage.get_cumulative_report_for_districts.return_value = \
            district_report_dtos
        presenter.response_state_cumulative_report.return_value = \
            state_cumulative_report_response

        # Act
        response = interactor.state_get_cumulative_report_wrapper(state_id=state_id,
            till_date=till_date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)
        assert response == expected_response


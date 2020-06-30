import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.state_get_day_report_interactor \
    import StateGetDayReportInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat


class TestStateGetDayReportInteractor:

    def test_get_day_report_when_invalid_state_id_given_raise_invalid_state_id_exception(self):

        # Arrange
        state_id = 1
        date = datetime.date.today()

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDayReportInteractor(storage=storage)

        storage.get_state_details.side_effect = InvalidStateId
        presenter.raise_invalid_state_id.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.state_get_day_report_wrapper(state_id=state_id,
                date=date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)
        presenter.raise_invalid_state_id.assert_called_once_with(
            state_id=state_id)

    def test_get_day_report_when_invalid_date_format_given_raise_invalid_date_format_exception(
            self, state_dto):

        # Arrange
        state_id = 1
        date = "2020-05-20"

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDayReportInteractor(storage=storage)

        storage.get_state_details.return_value = state_dto
        presenter.raise_invalid_date_format.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.state_get_day_report_wrapper(state_id=state_id,
                date=date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)

    def test_get_day_report(self, state_dto, day_report_dtos,
            response_state_day_report_dto, district_dtos, state_day_report_dto):

        # Arrange
        state_id = 1
        date = "02-05-2020"
        # date = datetime.date(year=2020, month=5, day=2)
        district_ids = [1,2]
        expected_output = response_state_day_report_dto

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDayReportInteractor(storage=storage)

        storage.get_state_details.return_value = state_dto
        storage.get_districts_for_state.return_value = district_dtos
        storage.get_day_report_districts.return_value = day_report_dtos
        presenter.response_state_day_report.return_value = expected_output

        # Act
        response = interactor.state_get_day_report_wrapper(state_id=state_id,
            date=date, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)
        storage.get_day_report_districts(district_ids=district_ids, date=date)
        presenter.response_state_day_report.assert_called_once_with(state_day_report_dto)
        assert response == expected_output


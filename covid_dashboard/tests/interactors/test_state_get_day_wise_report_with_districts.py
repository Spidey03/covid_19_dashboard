import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.state_get_day_wise_report_with_districts_interactor \
    import StateGetDayWiseReportWithDistrictsInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat


class TestGetDayWiseReportWithDistricts:

    def test_get_day_wise_report_with_district(self, state_dto, district_dtos, 
            district_day_report_dtos, district_day_wise_reports_of_a_state,
            response_district_day_wise_reports_of_a_state):

        # Arrange
        state_id=1
        district_ids = [1,2]
        expected_output = response_district_day_wise_reports_of_a_state

        storage = create_autospec(StateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateGetDayWiseReportWithDistrictsInteractor(storage=storage)

        storage.get_state_details.return_value = state_dto
        storage.get_districts_for_state.return_value = district_dtos
        storage.get_initial_and_final_dates.return_value = \
            datetime.date(year=2020, month=5, day=2), \
            datetime.date(year=2020, month=5, day=5)
        storage.get_day_wise_report_for_distrcts.return_value = district_day_report_dtos
        presenter.response_day_wise_report_with_districts.return_value = \
            response_district_day_wise_reports_of_a_state

        # Act
        output = interactor.state_get_day_wise_report_with_districts_wrapper(
            state_id=state_id, presenter=presenter)

        # Assert
        storage.get_state_details.assert_called_once_with(state_id=state_id)
        storage.get_districts_for_state.assert_called_once_with(
            state_id=state_id)
        storage.get_day_wise_report_for_distrcts.assert_called_once_with(
            district_ids=district_ids)
        presenter.response_day_wise_report_with_districts. \
            assert_called_once_with(district_day_wise_reports_of_a_state)
        assert output == expected_output

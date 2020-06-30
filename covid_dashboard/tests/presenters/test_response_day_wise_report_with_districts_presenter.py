from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation


class TestResponseStateDayWiseReportWithDistricts:

    def test_response_state_day_wise_report_with_districts(self,
            district_day_wise_reports_of_a_state, state_dto,
            response_state_day_wise_report_with_districts):

        # Arrange
        presenter = PresenterImplementation()
        expected_response = response_state_day_wise_report_with_districts

        # Act
        response = presenter.response_state_day_wise_report_with_districts(
            state_dto=state_dto, all_district_reports=district_day_wise_reports_of_a_state)

        # Assert
        assert response == expected_response
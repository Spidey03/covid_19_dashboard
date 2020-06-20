from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation


class TestRespnseStateCumulativeReport:

    def test_reponse_with_cumulative_state_report_dto(self, complete_state_cumulative_report_dto):

        # Arrange
        presenter = PresenterImplementation()
        expected_response = {
            'state_name': 'Andrapradesh',
            'districts': [
                {
                    'district_name': 'Kurnool',
                    'total_cases': 10,
                    'total_recovered_cases': 1,
                    'total_deaths': 3,
                    'active_cases': 6
                },
                {
                    'district_name': 'Nellore',
                    'total_cases': 0,
                    'total_recovered_cases': 0,
                    'total_deaths': 0,
                    'active_cases': 0
                }
            ],
            'total_cases': 10,
            'total_recovered_cases': 1,
            'total_deaths': 3,
            'active_cases': 6
        }

        # Act
        response = presenter.response_state_cumulative_report(
            complete_state_cumulative_report_dto)

        # Assert
        assert response == expected_response

from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation

class TestResponseStateDayWiseReport:

    def test_response_state_day_wise_report(self, state_day_wise_report_dtos):

        # Arrange
        presenter = PresenterImplementation()
        expected_response = {
            'daily_cumulative': [
                {
                    'date': '02-May-2020',
                    'total_cases': 10,
                    'total_recovered_cases': 5,
                    'total_deaths': 1,
                    'active_cases': 4
                },
                {
                    'date': '03-May-2020',
                    'total_cases': 10,
                    'total_recovered_cases': 5,
                    'total_deaths': 1,
                    'active_cases': 4
                },
                {
                    'date': '04-May-2020',
                    'total_cases': 15,
                    'total_recovered_cases': 8,
                    'total_deaths': 2,
                    'active_cases': 5
                },
                {
                    'date': '05-May-2020',
                    'total_cases': 17,
                    'total_recovered_cases': 9,
                    'total_deaths': 2,
                    'active_cases': 6
                }
            ]
        }

        # Act
        response = presenter.resonse_state_day_wise_report(state_day_wise_report_dtos)

        # Assert
        assert response == expected_response
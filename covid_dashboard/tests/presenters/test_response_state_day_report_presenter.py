from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation


class TestResponseStateGetDayReport:

    def test_response_state_get_day_report(self,
            day_report_dtos, state_day_report_dto):

        presenter = PresenterImplementation()
        expected_response = {
            'state_name': 'Andrapradesh',
            'total_cases': 15,
            'total_recovered_cases': 7,
            'total_deaths': 2,
            'districts': [
                {
                    'district_id': 1,
                    'total_cases': 10,
                    'total_recovered_cases': 5,
                    'total_deaths': 1
                },
                {
                    'district_id': 1,
                    'total_cases': 5,
                    'total_recovered_cases': 2,
                    'total_deaths': 1
                }
            ]
        }

        # Act
        response = presenter.response_state_day_report(state_day_report_dto)

        # Assert
        assert response == expected_response
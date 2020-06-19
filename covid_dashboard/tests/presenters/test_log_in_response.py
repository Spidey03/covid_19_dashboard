from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation


class TestLogInResponse:

    def test_log_in_response(self, user_auth_token_dto, login_response):
        # Arrange
        presenter = PresenterImplementation()

        # Act
        expected_login_response = \
            presenter.login_response(user_token_dto=user_auth_token_dto)

        # Assert
        assert expected_login_response == login_response
        
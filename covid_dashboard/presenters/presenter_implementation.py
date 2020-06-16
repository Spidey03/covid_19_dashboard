from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def raise_invalid_user_name(self):
        pass

    def raise_invalid_password(self):
        pass

    def login_response(self, user_token_dto):
        pass
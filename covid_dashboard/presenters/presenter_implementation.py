from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden
from covid_dashboard.constants.exception_messages import *
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface

class PresenterImplementation(PresenterInterface):

    def raise_invalid_user_name(self):
        raise NotFound(*INVALID_USERNAME)

    def raise_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)

    def login_response(self, user_token_dto):
        user_login_response = {
            "user_id": user_token_dto.user_id,
            "access_token": user_token_dto.access_token,
            "refresh_token": user_token_dto.refresh_token,
            "expires_in": user_token_dto.expires_in
        }
        return user_login_response


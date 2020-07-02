
from django_swagger_utils.drf_server.exceptions \
    import NotFound, Forbidden
from common.dtos import UserAuthTokensDTO
from covid_dashboard.constants.exception_messages \
    import INVALID_USERNAME, INVALID_PASSWORD, USER_NOT_ADMIN
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def get_response_login_user(self, tokens_dto: UserAuthTokensDTO):
        response = {
            "user_id":tokens_dto.user_id,
            "access_token":tokens_dto.access_token,
            "refresh_token":tokens_dto.refresh_token,
            "expires_in":tokens_dto.expires_in
        }
        return response

    def raiseinvalidusername(self):
        raise NotFound(*INVALID_USERNAME)

    def raiseinvalidpassword(self):
        raise NotFound(*INVALID_PASSWORD)

    def raise_user_not_admin(self):
        raise Forbidden(*USER_NOT_ADMIN)

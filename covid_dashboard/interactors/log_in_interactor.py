from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.interactors.storages.user_storage_interface \
    import UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.exceptions.exceptions \
    import InvalidUserName, InvalidPassword


class LogInInteractor:

    def __init__(self, storage=UserStorageInterface,
            oauth_storage=OAuth2SQLStorage):

        self.storage = storage
        self.oauth_storage=oauth_storage

    def login_wrapper(self, username: str, password: str,
            presenter = PresenterInterface):

        try:
            user_token_dto = self.login(username, password)
            return presenter.login_response(user_token_dto)
        except InvalidUserName:
            presenter.raise_invalid_user_name()
        except InvalidPassword:
            presenter.raise_invalid_password()

    def login(self, username: str, password: str):
        self.storage.check_is_user_name_valid(username)
        user_id = self.storage.check_is_password_valid(username, password)

        from common.oauth_user_auth_tokens_service\
            import OAuthUserAuthTokensService
        service = OAuthUserAuthTokensService(self.oauth_storage)
        user_token_dto = service.create_user_auth_tokens(user_id)

        return user_token_dto
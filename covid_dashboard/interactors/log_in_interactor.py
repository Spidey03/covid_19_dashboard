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

    def login_wrapper(self, user_name: str, password: str,
            presenter = PresenterInterface):

        try:
            user_token_dto = self.login(user_name, password)
        except InvalidUserName:
            presenter.raise_invalid_user_name()
        except InvalidPassword:
            presenter.raise_invalid_password()
        return presenter.login_response(user_token_dto)

    def login(self, user_name: str, password: str):
        self.storage.check_is_user_name_valid(user_name)
        self.storage.check_is_password_valid(user_name, password)

        from common.oauth_user_auth_tokens_service\
            import OAuthUserAuthTokensService
        service = OAuthUserAuthTokensService(self.oauth_storage)
        user_token_dto = service.create_user_auth_tokens(user_name)

        return user_token_dto
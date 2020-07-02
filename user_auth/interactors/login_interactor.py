from user_auth.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_auth.interactors.presenters.presenter_interface\
    import PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from user_auth.exceptions.exceptions\
    import InvalidUserName, InvalidPassword


class LoginUserInteractor:

    def __init__(self, storage=UserStorageInterface,
            oauth_storage=OAuth2SQLStorage,
            presenter=PresenterInterface):
        self.storage = storage
        self.oauth_storage=oauth_storage
        self.presenter = presenter

    def login_user(self, username: str, password: str):
        try:
            self.storage.is_valid_username(username)
        except InvalidUserName:
            raise self.presenter.raiseinvalidusername()

        try:
            user_id = self.storage.is_valid_password(
                username=username,
                password=password
                )
        except InvalidPassword:
            raise self.presenter.raiseinvalidpassword()
    
        from common.oauth_user_auth_tokens_service\
            import OAuthUserAuthTokensService
        
        service = OAuthUserAuthTokensService(self.oauth_storage)
        
        tokens_dto = service.create_user_auth_tokens(user_id)

        print(tokens_dto)
        
        return self.presenter.get_response_login_user(tokens_dto)
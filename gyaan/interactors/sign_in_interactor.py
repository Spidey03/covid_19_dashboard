from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth2_storage \
    import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service \
    import OAuthUserAuthTokensService
from gyaan.storages.storage_implementation import StorageImplementation
from gyaan.presenters.presenter_implementation import PresenterImplementaion

class SignInInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface,
                 oauth2_storage: OAuth2SQLStorage):
        self.storage = storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage

    def sign_in(self, username: str, password: str):
        is_valid_username = self.storage.validate_username(username=username)
        is_not_valid_username = not is_valid_username
        if is_not_valid_username:
            raise self.presenter.raise_invalid_username_exception()

        user_id = self.storage.validate_password_for_username(
            username=username, password=password)

        false = False
        is_not_valid_password = user_id == false
        if is_not_valid_password:
            raise self.presenter.raise_invalid_password_exception()

        oauth = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)

        user_auth_tokens_dto = oauth.create_user_auth_tokens(user_id=user_id)

        response = self.presenter.sign_in_response(
            user_auth_tokens_dto=user_auth_tokens_dto
        )
        print(user_auth_tokens_dto)
        return response

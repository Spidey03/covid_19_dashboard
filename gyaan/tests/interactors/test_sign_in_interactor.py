import datetime

from common.dtos import (
    UserAuthTokensDTO, AccessTokenDTO,
    RefreshTokenDTO, Application
)

from unittest.mock import create_autospec, patch

from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.sign_in_interactor import SignInInteractor
from gyaan.interactors.oauth.oauth2_interface \
    import OAuthUserAuthTokensServiceInterface, OAuth2SQLStorageInterface

oauth_response = UserAuthTokensDTO(user_id=1,
    access_token='ZOdzrfmffbO5TelgeIv3pdyejkgwZm',
    refresh_token='jQ5cqDucwV9pqvHYhxgXAfO1yTmV5z',
    expires_in=datetime.datetime(2052, 2, 3, 0, 10, 21, 245912))


@patch.object(OAuthUserAuthTokensServiceInterface, 'create_user_auth_tokens',
              return_value=oauth_response)
def test_sign_in_interactor(create_user_auth_tokens):
    # Arrange
    user_id = 1
    username = "gyaan"
    password = "gyaan"

    expected_output = {
        "user_id": 1,
        "access_token": "ZOdzrfmffbO5TelgeIv3pdyejkgwZm",
        "refresh_token": "jQ5cqDucwV9pqvHYhxgXAfO1yTmV5z",
        "expires_in": "2052-2-3 0:10:21.245912"
    }

    access_token_dto = AccessTokenDTO(
            access_token_id=1,
            token="ZOdzrfmffbO5TelgeIv3pdyejkgwZm",
            expires=datetime.datetime(2052, 2, 3, 0, 10, 21, 245912)
        )

    refresh_token_dto = RefreshTokenDTO(
            token="jQ5cqDucwV9pqvHYhxgXAfO1yTmV5z",
            access_token=1,
            user_id=1,
            revoked=datetime.datetime(2052, 2, 3, 0, 10, 21, 245912)
        )
    application_dto = Application(application_id=1)

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorageInterface)
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage = oauth2_storage
    )

    oauth2_storage.get_or_create_default_application.return_value = \
        application_dto, True
    oauth2_storage.create_access_token.return_value = access_token_dto
    oauth2_storage.create_refresh_token.return_value = refresh_token_dto
    storage.validate_username.return_value = True
    storage.validate_password_for_username.return_value = user_id
    presenter.sign_in_response.return_value = expected_output

    # Act
    actual_output = interactor.sign_in(username=username, password=password)

    # Assert
    assert actual_output == expected_output

    storage.validate_password_for_username.assert_called_once_with(
        username=username, password=password)
    presenter.sign_in_response.assert_called_once_with(
        user_auth_tokens_dto=oauth_response
    )

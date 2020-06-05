import pytest
import datetime
from unittest.mock import create_autospec
from mock import patch
from covid_dashboard.interactors.storages.user_storage_interface\
    import UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.login_interactor\
    import LoginUserInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service\
            import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService


expected_user_auth_token_dto = UserAuthTokensDTO(
    user_id=1,
    access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
    refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
    expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
)

def test_login_user_interactor_with_invalid_username():
    # Arrange
    username = 'user1'
    password = "password1"
    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()

    storage.is_valid_username.side_effect = InvalidUserName
    presenter.raiseinvalidusername.side_effect = InvalidUserName

    interactor = LoginUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    # Assert
    with pytest.raises(InvalidUserName):
        interactor.login_user(username=username, password=password)
    storage.is_valid_username.assert_called_once_with(username)


def test_login_user_interactor_with_invalid_password():
    # Arrange
    username = 'user1'
    password = "password2"
    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()

    storage.is_valid_username.return_value= None
    storage.is_valid_password.side_effect = InvalidPassword
    presenter.raiseinvalidpassword.side_effect = InvalidPassword

    interactor = LoginUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    # Assert
    with pytest.raises(InvalidPassword):
        interactor.login_user(username=username, password=password)
    storage.is_valid_username.assert_called_once_with(username)
    storage.is_valid_password.assert_called_once_with(username,password)


@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
    return_value=expected_user_auth_token_dto)
# @pytest.mark.django_db
def test_login_user_interactor_with_valid_details(useraccount):
    # Arrange
    username = 'user1'
    password = "password1"
    user_id = 1
    expires_in = datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    expected_token = {
        "user_id":user_id,
        "access_token":"HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        "refresh_token":"DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        "expires_in":expires_in
    }
    
    from common.oauth_user_auth_tokens_service\
            import OAuthUserAuthTokensService

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()

    storage.is_valid_username.return_value= None
    storage.is_valid_password.return_value = user_id
    presenter.get_response_login_user.return_value = expected_token
    
    interactor = LoginUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    # service = OAuthUserAuthTokensService(interactor.oauth_storage)

    # Act
    token = interactor.login_user(username=username, password=password)

    # Assert
    assert token == expected_token
    assert expected_user_auth_token_dto.user_id == user_id
    storage.is_valid_username.assert_called_once_with(username)
    storage.is_valid_password.assert_called_once_with(username,password)
    presenter.get_response_login_user.assert_called_once_with(expected_user_auth_token_dto)
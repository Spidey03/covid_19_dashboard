import pytest
import datetime
from mock import patch
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService
from covid_dashboard.interactors.storages.user_storage_interface \
    import UserStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.log_in_interactor import LogInInteractor
from covid_dashboard.exceptions.exceptions \
    import InvalidUserName, InvalidPassword

expected_user_auth_token_dto = UserAuthTokensDTO(
    user_id=1,
    access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
    refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
    expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
)

def test_login_interactor_with_invalid_user_name_raises_invalid_user_name():
    # Arange
    user_name = "parker"
    password = "12345"

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()

    storage.check_is_user_name_valid.side_effect = InvalidUserName
    presenter.raise_invalid_user_name.side_effect = InvalidUserName
    interactor = LogInInteractor(
        storage=storage,
        oauth_storage=oauth_storage
    )

    # Act
    with pytest.raises(InvalidUserName):
        interactor.login_wrapper(user_name=user_name, password=password,
            presenter=presenter)


def test_login_interactor_with_invalid_password_raises_invalid_password():
    # Arange
    user_name = "parker"
    password = "12345"

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()

    storage.check_is_password_valid.side_effect = InvalidPassword
    presenter.raise_invalid_password.side_effect = InvalidPassword
    interactor = LogInInteractor(
        storage=storage,
        oauth_storage=oauth_storage
    )

    # Act
    with pytest.raises(InvalidPassword):
        interactor.login_wrapper(user_name=user_name, password=password,
            presenter=presenter)


@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
    return_value=expected_user_auth_token_dto)
def test_login_interactor_with_valid_details_returns_token_dto(bbc):
    # Arange
    import datetime
    from common.dtos import UserAuthTokensDTO
    user_name = "parker"
    password = "12345"
    expected_user_auth_token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    )
    expected_response = {
        "user_id":1,
        "access_token":"HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        "refresh_token":"DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        "expires_in":datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    }

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    presenter.login_response.return_value = expected_response

    
    interactor = LogInInteractor(
        storage=storage,
        oauth_storage=oauth_storage
    )

    # Act
    response = interactor.login_wrapper(user_name=user_name,
        password=password, presenter=presenter)

    # Assert
    assert response == expected_response
    presenter.login_response.assert_called_once_with(expected_user_auth_token_dto)

import datetime
import pytest
from common.dtos import UserAuthTokensDTO

@pytest.fixture
def user_auth_token_dto():
    user_auth_token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    )
    return user_auth_token_dto

@pytest.fixture
def login_response():
    login_response = {
        "user_id":1,
        "access_token":"HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        "refresh_token":"DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        "expires_in":datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    }
    return login_response
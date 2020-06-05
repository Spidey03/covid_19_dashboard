import pytest
import datetime
from common.dtos import UserAuthTokensDTO
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import *
    
    
def test_login_user_presenter_returns_access_token_dict():
    # Arrange
    token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    )
    presenter = PresenterImplementation()
    expected_response = {
        "user_id":1,
        "access_token":"HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        "refresh_token":"DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        "expires_in":datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    }

    # Act
    response = presenter.get_response_login_user(token_dto)

    # Arrange
    assert response == expected_response
import datetime
import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from common.dtos import UserAuthTokensDTO

from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion
from gyaan.constants.exception_messages import (
    INVALID_PASSWORD,
    INVALID_USERNAME
)

def test_sign_in_with_valid_details_returns_access_token():
    # Arrange
    oauth_response = UserAuthTokensDTO(user_id=1,
        access_token='1234',
        refresh_token='1234',
        expires_in=datetime.datetime(2020, 5, 27, 5, 29, 29, 705022)
    )
    expected_output = {
        "user_id": 1,
        "access_token": "1234",
        "refresh_token": "1234",
        "expires_in": '2020-05-27 05:29:29.705022'
    }
    presenter = PresenterImplementaion()

    # Act
    actual_output = presenter.sign_in_response(
        user_auth_tokens_dto=oauth_response
    )

    # Assert
    assert actual_output == expected_output

def test_sign_in_with_invalid_username_raises_exception():
    # Arrange
    presenter = PresenterImplementaion()
    exception_message = INVALID_USERNAME[0]
    exception_res_status = INVALID_USERNAME[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_username_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

def test_sign_in_with_invalid_password_raises_exception():
    # Arrange
    presenter = PresenterImplementaion()
    exception_message = INVALID_PASSWORD[0]
    exception_res_status = INVALID_PASSWORD[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_password_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.user_storage_implementation\
    import UserStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword

@pytest.mark.django_db
def test_is_valid_username_with_invalid_user_raises_exception():
    # Arrange
    username = "user1"
    password = "password1"
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUserName):
        storage.is_valid_username(username=username)


@pytest.mark.django_db
def test_is_valid_username_with_valid_user(useraccount):
    username = "user1"
    password = "password1"
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    result = storage.is_valid_username(username=username)

    # Assert
    assert result == None


@pytest.mark.django_db
def test_is_valid_password_with_invalid_password_raises_exception(useraccount):
    username = "user1"
    password = "password2"
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        storage.is_valid_password(username=username, password=password)


@pytest.mark.django_db
def test_is_valid_password_with_valid_password_returns_user_id(useraccount):
    username = "user1"
    password = "password1"
    user_id = 1
    storage = UserStorageImplementation()

    # Act
    result = storage.is_valid_password(username=username, password=password)

    # Assert
    assert user_id == result

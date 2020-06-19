import pytest
from covid_dashboard.storages.user_storage_implementation \
    import UserStorageImplementation
from covid_dashboard.exceptions.exceptions \
    import InvalidUserName, InvalidPassword

@pytest.mark.django_db
def test_check_username_valid_when_user_does_not_exists():
    # Arrange
    username = 'Loki'
    password = 'Asgardian84'
    
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUserName):
        user_storage.check_is_password_valid(username, password)

@pytest.mark.django_db
def test_check_username_valid_when_user_exists_and_password_wrong_raises_invalid_password_exception(user):
    # Arrange
    username = 'Loki'
    password = 'hmm'
    
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        user_storage.check_is_password_valid(username, password)

@pytest.mark.django_db
def test_check_username_valid_when_user_exists_and_password_correct(user):
    # Arrange
    username = 'Loki'
    password = 'Asgardian84'
    expected_result = None
    
    user_storage = UserStorageImplementation()

    # Act
    result = user_storage.check_is_password_valid(username, password)

    # Assert
    assert result == expected_result
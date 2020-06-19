import pytest
from covid_dashboard.storages.user_storage_implementation \
    import UserStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidUserName

@pytest.mark.django_db
def test_check_username_valid_when_user_does_not_exists():
    # Arrange
    username = 'Loki'
    password = 'Asgardian84'
    
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUserName):
        user_storage.check_is_user_name_valid(username)

@pytest.mark.django_db
def test_check_username_valid_when_user_exists(user):
    # Arrange
    username = 'Loki'
    password = 'Asgardian84'
    expected_result = None
    
    user_storage = UserStorageImplementation()

    # Act
    result = user_storage.check_is_user_name_valid(username)

    # Assert
    assert result == expected_result
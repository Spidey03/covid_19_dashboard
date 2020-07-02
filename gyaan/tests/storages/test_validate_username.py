import pytest

from gyaan.storages.storage_implementation \
    import StorageImplementation

@pytest.mark.django_db
def test_valid_username_with_valid_details(create_users):
    # Arrange
    username = "gyaan"
    storage = StorageImplementation()
    expected_output = True

    # Act
    actual_output = storage.validate_username(username=username)

    # Assert
    assert actual_output == expected_output

@pytest.mark.django_db
def test_valid_username_and_password_with_valid_details(create_users):
    # Arrange
    username = "gyaan"
    password = "gyaan"
    storage = StorageImplementation()
    expected_output = 1

    # Act
    actual_output = storage.validate_password_for_username(
        username=username, password=password)

    # Assert
    assert actual_output == expected_output

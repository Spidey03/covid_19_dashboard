import datetime
import pytest

from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.interactors.storages.dtos import (
    GetPostDto, UserDto, DomainDto, CommentDto, AnswerDto,
    UserRequestedDomainDto, UserDomainPostDto
)

@pytest.mark.django_db
def test_get_user_dto_with_valid_details(create_users):
    # Arrange
    user_id = 1
    expected_output = UserDto(
        user_id=1,
        name="Mahesh",
        profile_pic="mahesh@abc.com"
    )

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_user_dto(user_id=user_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_following_domain_dtos_with_valid_details(create_users,
        populate_database, populate_domain_members):
    # Arrange
    user_id = 1
    expected_output = [DomainDto(
        domain_id=1,
        name='Django',
        picture='dkfajh',
        members_dtos=[],
        request_dtos=[]
    )]

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_following_domain_dtos(user_id=user_id)

    # Assert
    assert actual_output == expected_output

@pytest.mark.django_db
def test_get_some_domain_dtos_with_valid_details(
        create_users, populate_database):
    # Arrange
    user_id = 1
    expected_output = [DomainDto(
        domain_id=1,
        name='Django',
        picture='dkfajh',
        members_dtos=[],
        request_dtos=[]
    )]

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_some_domain_dtos()

    # Assert
    assert actual_output == expected_output

@pytest.mark.django_db
def test_get_user_requested_domain_dtos_with_valid_details(
        create_users, populate_database, create_domain_requests):
    # Arrange
    user_id = 1
    expected_output = [UserRequestedDomainDto(
        user_id=2, domain_id=1, is_requested=True)
    ]

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_user_requested_domain_dtos(user_id=user_id)

    # Assert
    assert actual_output == expected_output



@pytest.mark.django_db
def test_get_approved_posts_of_user_in_eachdomain_dtos_with_valid_details(
        create_users, populate_database, create_domain_requests):
    # Arrange
    user_id = 1
    expected_output = [UserDomainPostDto(
        domain_id=1, name='Django',
        picture='dkfajh', posts_count=1)
    ]
    storage = StorageImplementation()

    # Act
    actual_output = storage.get_approved_posts_in_each_domain_dtos(
        user_id=user_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_pending_posts_of_user_in_eachdomain_dtos_with_valid_details(
        create_users, populate_database, create_domain_requests):
    # Arrange
    user_id = 1
    expected_output = []
    storage = StorageImplementation()

    # Act
    actual_output = storage.get_pending_posts_in_each_domain_dtos(
        user_id=user_id)

    # Assert
    assert actual_output == expected_output

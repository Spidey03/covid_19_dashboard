import pytest

from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.models import Post, PostVersion, Domain
from gyaan.interactors.storages.dtos import (
    DomainDetailsDto, DomainExpertsDetailsDto, UserDto
)


@pytest.mark.django_db
def test_get_domain_details_with_experts_dtos_with_valid_details(
        create_users, create_domains, create_domain_experts):
    # Arrange
    domain_id = 1
    domain_details_dto = DomainDetailsDto(
        domain_id=1,
        name="Django",
        description="django",
        picture="dkfajh",
        no_of_followers=0,
        total_posts=0,
        likes=0
    )

    domain_expert_details_dto = DomainExpertsDetailsDto(
        total_experts=1,
        domain_experts=[UserDto(
            user_id=1,
            name="Mahesh",
            profile_pic="mahesh@abc.com"
        )]
    )

    storage = DomainStorageImplementation()

    # Act
    actual_output1, actual_output2 = storage.get_domain_details_dto_with_experts_dtos(
        domain_id=domain_id
    )

    # Assert
    assert actual_output1 == domain_details_dto
    assert actual_output2 == domain_expert_details_dto
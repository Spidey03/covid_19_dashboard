import pytest

from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.models import Post, PostVersion

@pytest.mark.django_db
def test_create_post_with_valid_details(
        create_users, create_domains, create_posts):
    # Arrange
    user_id = 1
    title = "First post"
    description = "dummy"
    domain_id = 1
    tag_ids = [1,2,3]
    status = "PENDING"
    storage = StorageImplementation()

    # Act
    storage.create_post(
        user_id=user_id,
        title=title,
        description=description,
        domain_id=domain_id,
        tag_ids=tag_ids
    )

    # Assert
    post = PostVersion.objects.filter(id=1) \
        .select_related('post').first()

    assert post.title == title
    assert post.description == description
    assert post.status == status
    assert post.post.posted_by_id == user_id
    assert post.post.domain_id == domain_id
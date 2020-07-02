import pytest

from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.models import Reaction

@pytest.mark.django_db
def test_create_reaction_to_post_with_valid_details(
        create_users, create_domains, create_posts):
    # Arrange
    user_id=1
    entity_id = 1
    entity_type="post"
    true = True
    storage = StorageImplementation()

    # Act
    storage.create_reaction(user_id=user_id,
                            entity_type=entity_type,
                            entity_id=entity_id)

    # Assert
    reaction = Reaction.objects.filter(post_id=entity_id) \
        .select_related('user').first()

    assert reaction.user_id == user_id
    assert reaction.is_reacted == true
    assert reaction.post_id == entity_id


@pytest.mark.django_db
def test_create_reaction_to_comment_with_valid_details(
        create_users, create_domains,
        create_posts, create_comments):
    # Arrange
    user_id=1
    entity_id = 1
    entity_type="comment"
    true = True
    storage = StorageImplementation()

    # Act
    storage.create_reaction(user_id=user_id,
                            entity_type=entity_type,
                            entity_id=entity_id)

    # Assert
    reaction = Reaction.objects.filter(comment_id=entity_id) \
        .select_related('user').first()

    assert reaction.user_id == user_id
    assert reaction.comment_id == entity_id
    assert reaction.is_reacted == true
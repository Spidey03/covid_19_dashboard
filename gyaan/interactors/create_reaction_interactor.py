from typing import List
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.constants.enums import ReactionEntityType

class CreateReactionInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_reaction(self, user_id: int, entity_type: str,
                    entity_id: int):

        is_post_entity = entity_type == ReactionEntityType.Post.value

        if is_post_entity:
            self._create_reaction_to_post(user_id,entity_id)
        else:
            self._create_reaction_to_comment(user_id, entity_id)


    def _create_reaction_to_post(self, user_id, entity_id):

        is_not_valid_post_id = not self.storage.validate_post_id(
            post_id=entity_id
        )
        if is_not_valid_post_id:
            self.presenter.raise_exception_for_invalid_post_id()
            return

        self.storage.create_reaction_to_post(
            user_id=user_id,
            entity_id=entity_id,
        )


    def _create_reaction_to_comment(self, user_id, entity_id):
        is_not_valid_comment_id = not self.storage.validate_comment_id(
            comment_id=entity_id
        )
        if is_not_valid_comment_id:
            self.presenter.raise_exception_for_invalid_comment_id()
            return

        self.storage.create_reaction_to_comment(
            user_id=user_id,
            entity_id=entity_id
        )

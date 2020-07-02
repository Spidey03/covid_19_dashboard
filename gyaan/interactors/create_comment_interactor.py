from gyaan.constants.enums import ReactionEntityType
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface

class CreateCommentInteractor:

    def __init__(self, storage=StorageInterface,
                 post_presenter=PostPresenterInterface):
        self.storage = storage
        self.post_presenter = post_presenter

    def create_comment(self, user_id: int, entity_type: str,
                       entity_id: int, content: str):

        is_post_entity = entity_type == ReactionEntityType.Post.value

        if is_post_entity:
            self._create_comment_to_post(user_id,entity_id, content)
        else:
            self._create_reply_to_comment(user_id, entity_id, content)


    def _create_comment_to_post(self, user_id, entity_id, content):
        is_not_valid_post_id = not self.storage.validate_post_id(
            post_id=entity_id
        )
        if is_not_valid_post_id:
            self.post_presenter.raise_exception_for_invalid_post_id()
            return

        self.storage.create_comment_to_post(
            user_id=user_id,
            entity_id=entity_id,
            content=content
        )


    def _create_reply_to_comment(self, user_id, entity_id, content):

        is_not_valid_comment_id = not self.storage.validate_comment_id(
            comment_id=entity_id
        )
        if is_not_valid_comment_id:
            self.post_presenter.raise_exception_for_invalid_comment_id()
            return

        parent_comment_id = self.storage.get_parent_comment_id(
            comment_id=entity_id
        )

        if parent_comment_id:
            entity_id = parent_comment_id

        self.storage.create_reply_to_comment(
            user_id=user_id,
            entity_id=entity_id,
            content=content
        )

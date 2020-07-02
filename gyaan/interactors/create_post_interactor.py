from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from typing import List

class CreatePostInteractor:

    def __init__(self, post_storage: PostStorageInterface,
                 post_presenter: PostPresenterInterface):
        self.post_storage = post_storage
        self.post_presenter = post_presenter

    def create_post(self, user_id: int, title: str, domain_id: int,
                    content: str, tag_ids: List[int]):

        is_not_valid_domain_id = not self.post_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            self.post_presenter.raise_exception_for_invalid_domain_id()
            return

        self.post_storage.create_post(
            user_id=user_id,
            title=title,
            content=content,
            domain_id=domain_id,
            tag_ids=tag_ids
        )

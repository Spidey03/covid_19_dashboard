from typing import List
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.exceptions.exceptions import InvalidPostIdsException

class GetPostsInteractor:

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int]):

        # TODO: VALIDATE POST IDS
        valid_post_ids = self.storage.get_valid_post_ids(post_ids)
        invalid_post_ids = list(set(post_ids) - set(valid_post_ids))
        if invalid_post_ids:
            raise InvalidPostIdsException(invalid_post_ids)

        
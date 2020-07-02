from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from typing import List

class InvalidDomainId(Exception):
    pass

class CreatePostInteractor:

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage


    def create_post_wrapper(self, user_id: int, title: str, domain_id: int,
                            content: str, tag_ids: List[int],
                            post_presenter: PostPresenterInterface):
        try:
            self.create_post(user_id=user_id, title=title,
                             domain_id=domain_id, content=content,
                             tag_ids=tag_ids)

        except InvalidDomainId:
            raise post_presenter.raise_exception_for_invalid_domain_id()



    def create_post(self, user_id: int, title: str, domain_id: int,
                    content: str, tag_ids: List[int]):

        is_not_valid_domain_id = not self.post_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            raise InvalidDomainId()

        self.post_storage.create_post(
            user_id=user_id,
            title=title,
            content=content,
            domain_id=domain_id,
            tag_ids=tag_ids
        )

"""
TODO: Break Down the use case
 - date: valid date and format
 - meal_type: exists or not and is it available on that prticaular datet
 - amount: selected amount is in range for that particular meal_type

"""
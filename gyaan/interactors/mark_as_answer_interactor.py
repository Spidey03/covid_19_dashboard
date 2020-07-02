from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface

class MarkAsAnswerInteractor:

    def __init__(self, storage=StorageInterface,
                 presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def mark_as_answer(self, user_id: int, comment_id: int):

        is_not_valid_comment_id = not self.storage.validate_comment_id(
            comment_id=comment_id
        )
        if is_not_valid_comment_id:
            self.presenter.raise_exception_for_invalid_comment_id()
            return

        self.storage.mark_as_answer(user_id, comment_id)

from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.mixins import FormValidationMixin


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def submit_form_response_wrapper(self, form_id: int, question_id: int,
            presenter: PresenterInterface):

        self.validate_for_live_form(form_id=form_id)

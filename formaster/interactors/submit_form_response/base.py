from abc import abstractmethod
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.mixins import FormValidationMixin
from formaster.exceptions.exceptions\
    import FormDoesNotExist, FormClosed, QuestionDoesNotBelongToForm,\
        InvalidUserResponseSubmit


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface, form_id: int,
            question_id: int, user_id: int):

        self.storage = storage
        self.user_id = user_id
        self.question_id = question_id
        self.form_id = form_id

    def submit_form_response_wrapper(self, presenter: PresenterInterface):

        try:
            user_response_id = self.submit_form_response()
            return presenter.submit_form_response(
                user_response_id=user_response_id)
        except FormDoesNotExist:
            presenter.raise_form_does_not_exist()
        except FormClosed:
            presenter.raise_form_is_closed()
        except QuestionDoesNotBelongToForm:
            presenter.raise_question_does_not_belong_to_form()
        except InvalidUserResponseSubmit:
            presenter.raise_invalid_user_response()

    def submit_form_response(self):

        self.validate_for_live_form(form_id=self.form_id)
        self.storage.validate_question_id_with_form(question_id=self.question_id,
            form_id=self.form_id)
        self._validate_user_response()
        user_response_id = self._create_user_response()
        return user_response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _create_user_response(self):
        pass

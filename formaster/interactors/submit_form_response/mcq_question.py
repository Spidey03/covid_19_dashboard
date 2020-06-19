from abc import abstractmethod
from formaster.interactors.submit_form_response.base \
    import BaseSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.mixins import FormValidationMixin
from formaster.exceptions.exceptions\
    import FormDoesNotExist, FormClosed, QuestionDoesNotBelongToForm,\
        InvalidUserResponseSubmit
from formaster.interactors.storages.dtos import UserMCQResponseDto


class MCQuestionSubmitFormResponseInteractor(BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, form_id: int,
            question_id: int, user_id: int, option_id: int):

        super().__init__(storage=storage, form_id=form_id,
            question_id=question_id, user_id=user_id)
        self.option_id = option_id
        

    def _validate_user_response(self):
        option_ids = self.storage.get_option_ids_for_question(self.question_id)
        if self.option_id not in option_ids:
            raise InvalidUserResponseSubmit()

    def _create_user_response(self):
        user_response_dto = UserMCQResponseDto(
            user_id=self.user_id,
            question_id=self.question_id,
            option_id=self.option_id
        )
        response_id = self.storage.create_user_mcq_response(user_response_dto)
        return response_id


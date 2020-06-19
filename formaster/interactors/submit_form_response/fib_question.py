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
from formaster.interactors.storages.dtos import UserFIBResponseDto


class FIBQuestionSubmitFormResponseInteractor(BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, form_id: int,
            question_id: int, user_id: int, answer: int):

        super().__init__(storage=storage, form_id=form_id,
            question_id=question_id, user_id=user_id)
        self.answer = answer

    
    def _validate_user_response(self):
        answer = self.storage.get_valid_answer_for_question(self.question_id)
        if self.answer != answer:
            raise InvalidUserResponseSubmit()

    def _create_user_response(self):
        user_response_dto = UserFIBResponseDto(
            user_id=self.user_id,
            question_id=self.question_id,
            answer=self.answer
        )
        response_id = self.storage.create_user_fib_response(user_response_dto)
        return response_id

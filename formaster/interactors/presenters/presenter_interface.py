from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_form_does_not_exist(self):
        pass

    @abstractmethod
    def raise_form_is_closed(self):
        pass

    @abstractmethod
    def raise_question_does_not_belong_to_form(self):
        pass

    @abstractmethod
    def raise_invalid_user_response(self):
        pass

    @abstractmethod
    def submit_form_response(self, user_response_id: int):
        pass

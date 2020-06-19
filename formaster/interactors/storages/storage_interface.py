from abc import ABC
from abc import abstractmethod
from typing import List
from formaster.interactors.storages.dtos import *


class StorageInterface(ABC):

    @abstractmethod
    def validate_question_id_with_form(self, question_id: int, form_id: int):
        pass

    @abstractmethod
    def get_form(self, form_id: int) -> bool:
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id: int) -> List[int]:
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_mcq_response: UserMCQResponseDto) -> int:
        pass

    @abstractmethod
    def get_valid_answer_for_question(self, question_id:int) -> str:
        pass

    @abstractmethod
    def create_user_fib_response(self, user_fib_response: UserFIBResponseDto) -> int:
        pass
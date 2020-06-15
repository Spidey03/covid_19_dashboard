from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_user_name(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def login_response(self, user_token_dto):
        pass
from abc import ABC
from abc import abstractmethod


class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: str):
        pass

    @abstractmethod
    def is_valid_password(self, username: str, password: str):
        pass
from abc import ABC
from abc import abstractmethod
from user_auth.interactors.storages.dtos import UserDto

class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: str):
        pass

    @abstractmethod
    def is_valid_password(self, username: str, password: str):
        pass

    @abstractmethod
    def get_user_details_dto(self, user_id: int) -> UserDto:
        pass
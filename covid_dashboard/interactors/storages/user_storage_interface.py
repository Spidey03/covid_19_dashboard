from abc import ABC
from abc import abstractmethod

class UserStorageInterface(ABC):

    @abstractmethod
    def check_is_user_name_valid(self, user_name: str):
        pass

    
    @abstractmethod
    def check_is_password_valid(self, user_name: str, password: str):
        pass
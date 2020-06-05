from abc import ABC
from abc import abstractmethod
from covid_dashboard.models import User
from covid_dashboard.interactors.storages.user_storage_interface\
    import UserStorageInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword


class UserStorageImplementation(UserStorageInterface):

    def is_valid_username(self, username: str):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName

    def is_valid_password(self, username: str, password: str):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName

        if not user.check_password(password):
            raise InvalidPassword
        return user.id
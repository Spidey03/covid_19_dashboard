from covid_dashboard.models import User
from covid_dashboard.interactors.storages.user_storage_interface \
    import UserStorageInterface
from covid_dashboard.exceptions.exceptions \
    import InvalidUserName, InvalidPassword

class UserStorageImplementation(UserStorageInterface):

    def check_is_user_name_valid(self, username: str):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName


    def check_is_password_valid(self, username: str, password: str) -> int:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName
        print("*7"*10)
        print(user.password)
        is_valid_password = user.check_password(password)
        print(is_valid_password)
        print("*7"*10)
        if not is_valid_password:
            raise InvalidPassword
        return user.id
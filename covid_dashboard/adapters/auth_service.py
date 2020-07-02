class AuthService:

    @property
    def interface(self):
        from user_auth.interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def get_user_dto(self, user_id: int):
        user_dto = self.interface.get_user_dto(user_id=user_id)
        return user_dto

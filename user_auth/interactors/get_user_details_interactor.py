from typing import List

from covid_dashboard_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface


class GetUserDetailsInteractor:

    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def get_user_details_wrapper(self, user_id: int):
        user_dto = self.get_user_details_dto(user_id=user_id)
        return user_dto

    def get_user_details_dto(self, user_id: int):
        user_dto = self.storage.get_user_details_dto(user_id=user_id)
        return user_dto

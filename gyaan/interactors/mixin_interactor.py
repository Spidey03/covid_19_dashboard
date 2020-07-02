from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface

from gyaan.exceptions.custom_exceptions import \
    InvalidLimit, InvalidOffset, UserNotDomainMember

class InvalidDomainId(Exception):
    def __init__(self, domain_id):
        self.domain_id = domain_id

class DomainValidationMixin:

    def validate_domain_id(self, domain_id: int):
        is_valid_domain = self.post_storage.validate_domain_id(
            domain_id=domain_id)
        if not is_valid_domain:
            raise InvalidDomainId(domain_id=domain_id)

    def is_user_following_domain(self, user_id: int, domain_id: int):
        is_user_following_domain = self.post_storage.is_user_following_domain(
        user_id=user_id, domain_id=domain_id)
        if not is_user_following_domain:
            raise UserNotDomainMember


    def validate_offset_and_limit(self, offset: int, limit: int):
        is_valid_offset = self.is_valid_parameter(offset)
        if not is_valid_offset:
            raise InvalidOffset

        is_valid_limit = self.is_valid_parameter(limit)
        if not is_valid_limit:
            raise InvalidLimit

    @staticmethod
    def is_valid_parameter(parameter):
        bool_feild = parameter >= 0
        return bool_feild
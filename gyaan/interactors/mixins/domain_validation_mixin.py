from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.exceptions.custom_exceptions import InvalidDomainId


class DomainValidationMixin:

    def __init__(self, domain_storage: DomainStorageInterface):
        self.domain_storage = domain_storage

    def validate_domain_id(self, domain_id: int):
        is_valid_domain = self.domain_storage.validate_domain_id(domain_id)
        if not is_valid_domain:
            raise InvalidDomainId
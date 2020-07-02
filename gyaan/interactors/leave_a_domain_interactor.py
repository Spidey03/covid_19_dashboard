from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface

class LeaveDomainInteractor:

    def __init__(self, domain_storage: DomainStorageInterface,
                 domain_presenter: DomainPresenterInterface):
        self.domain_presenter = domain_presenter
        self.domain_storage = domain_storage

    def leave_a_domain(self, user_id: int, domain_id: int):

        is_not_valid_domain_id = not self.domain_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            self.domain_presenter.raise_exception_for_invalid_domain_id()
            return


        self.domain_storage.leave_a_domain(
            user_id=user_id, domain_id=domain_id
        )
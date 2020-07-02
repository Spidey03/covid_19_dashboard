from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.constants.enums import RequestStatus

class ApproveOrRejectRequestInteractor:

    def __init__(self, domain_storage=DomainStorageInterface,
                 domain_presenter=DomainPresenterInterface):
        self.domain_storage = domain_storage
        self.domain_presenter = domain_presenter

    def approve_or_reject_request(self, user_id: int, request_id: int,
                                  accept_status: str):

        is_request_accepted = accept_status == RequestStatus.ACCEPTED.value
        if is_request_accepted:
            self.domain_storage.approve_a_join_request(
                user_id, request_id)
        else:
            self.domain_storage.reject_a_join_request(
                user_id, request_id)

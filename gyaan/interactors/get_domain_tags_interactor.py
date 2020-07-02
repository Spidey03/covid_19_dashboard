from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface

class GetDomainTagsInteractor:

    def __init__(self, domain_storage: DomainStorageInterface,
                 domain_presenter: DomainPresenterInterface):
        self.domain_storage = domain_storage
        self.domain_presenter = domain_presenter

    def get_domain_tags(self, domain_id: int):

        is_not_valid_domain_id = not self.domain_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            self.domain_presenter.raise_exception_for_invalid_domain_id()
            return

        tags_dto = self.domain_storage.get_domain_tags_dto(domain_id)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(tags_dto)

        response = self.domain_presenter.get_domain_tags_response(
            tags_dto=tags_dto
        )

        return response
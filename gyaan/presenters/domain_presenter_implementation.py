from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface

from gyaan.interactors.storages.dtos_v2 import *

class DomainPresenterImplementation(DomainPresenterInterface):

    def raise_exception_for_invalid_domain_id(self):
        raise NotFound(*INVALID_DOMAIN_ID)

    def get_domain_tags_response(
            self, tags_dto: List[TagDto]):
        tags_dict = [self._convert_tag_dto_to_dict(tag) for tag in tags_dto]
        return tags_dict

    @staticmethod
    def _convert_tag_dto_to_dict(tag):
        return {
            "id": tag.tag_id,
            "name": tag.name
        }
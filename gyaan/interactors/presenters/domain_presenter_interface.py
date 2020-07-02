from abc import ABC, abstractmethod

from typing import List

from gyaan.interactors.storages.dtos import (
    PendingPostMetrics, DomainJoinRequestWithCountDto
)
from gyaan.interactors.storages.dtos_v2 import (
    TagDto
)

class DomainPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_domain_id(self):
        pass

    @abstractmethod
    def get_domain_tags_response(
            self, tags_dto: List[TagDto]):
        pass

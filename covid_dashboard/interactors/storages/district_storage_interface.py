from abc import ABC
from abc import abstractmethod

class DistrictStorageInterface(ABC):

    @abstractmethod
    def check_is_district_id_valid(self, district_id: int) -> bool:
        pass

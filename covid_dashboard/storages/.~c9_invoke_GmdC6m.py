import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from covid_dashboard.models import State, District, Stats
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos \
    import StateDto, DistrictDto, DistrictReportDto

class StateStorageImplementation(StateStorageInterface):

    def get_state_details(self, state_id: int) -> StateDto:
        try:
            state = State.objects.get(id=state_id)
        except State.DoesNotExist:
            raise InvalidStateId

        state_dto = StateDto(
                state_id=state.id,
                state_name=state.name
            )
        return state_dto

    def get_districts_for_state(self, state_id: int) -> List[DistrictDto]:
        districts = District.objects.filter(state_id=state_id)
        district_dtos = []
        for district in districts:
            district_dtos.append(
                DistrictDto(
                    district_id=district.id,
                    district_name=district.name
                )
            )
        return district_dtos

    def get_cumulative_report_for_districts(self, district_ids: List[int],
            till_date: datetime.date) -> List[DistrictReportDto]:

        report_query_set = Mandal.objects.values('district_id')\
                                 .filter

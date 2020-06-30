import datetime
from typing import List
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.mixins.extract_report import ExtractReport
from covid_dashboard.interactors.mixins.validations import ValidationMixin
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat
from covid_dashboard.interactors.storages.dtos \
    import StateDto, DistrictDayReportDto, StateDayReportDto


class StateGetDayReportInteractor(ValidationMixin, ExtractReport):

    def __init__(self, storage: StateStorageInterface):

        self.storage = storage

    def state_get_day_report_wrapper(self, presenter: PresenterInterface,
            date: datetime.date, state_id=1):

        try:
            state_get_day_report = \
                self.state_get_day_report(state_id=state_id, date=date)
            response = presenter.response_state_day_report(state_get_day_report)
            return response
        except InvalidStateId:
            presenter.raise_invalid_state_id(state_id=state_id)
        except InvalidDateFormat:
            presenter.raise_invalid_date_format()

    def state_get_day_report(self, state_id: int, date: datetime.date):

        state_dto = self.storage.get_state_details(state_id=state_id)
        self.validate_date_format(date=date)
        district_dtos = self.storage.get_districts_for_state(
            state_id=state_id)
        district_ids = [district.district_id for district in district_dtos]
        day_report_dtos = self.storage.get_day_report_districts(
            district_ids=district_ids, date=date)
        print(day_report_dtos)
        state_day_report_dto = self._convert_to_state_day_report(state_dto=state_dto,
            day_report_dtos=day_report_dtos)
        print(state_day_report_dto)
        return state_day_report_dto

    def _convert_to_state_day_report(self, state_dto: StateDto,
            day_report_dtos: List[DistrictDayReportDto]) -> StateDayReportDto:

        total_confirmed, total_recovered, total_deaths = 0, 0, 0
        for report in day_report_dtos:
            confirmed, recovered, deaths = self.extract_report(report)
            total_confirmed += confirmed
            total_recovered += recovered
            total_deaths += deaths

        state_day_report_dto = StateDayReportDto(
            state_name=state_dto.state_name,
            district_reports=day_report_dtos,
            total_confirmed=total_confirmed,
            total_recovered=total_recovered,
            total_deaths=total_deaths
        )
        return state_day_report_dto

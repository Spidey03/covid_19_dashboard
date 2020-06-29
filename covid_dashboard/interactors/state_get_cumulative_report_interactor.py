import datetime
from typing import List
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.storages.dtos import DistrictReportDto, \
    DistrictTotalReportDto, TotalReportDto, CompleteStateCumulativeReportDto
from covid_dashboard.interactors.mixins.validations import ValidationMixin
from covid_dashboard.interactors.mixins.extract_report \
    import ExtractReport
from covid_dashboard.exceptions.exceptions \
    import InvalidStateId, InvalidDateFormat


class StateGetCumulativeReportInteractor(ValidationMixin, ExtractReport):

    def __init__(self, storage: StateStorageInterface):

        self.storage = storage

    def state_get_cumulative_report_wrapper(self, till_date: datetime.date,
            presenter: PresenterInterface, state_id=1):

        try:
            state_cumulative_report_dto = \
                self.state_get_cumulative_report(state_id=state_id,
                    till_date=till_date)
            return presenter.response_state_cumulative_report(
                state_cumulative_report_dto)
        except InvalidStateId:
            presenter.raise_invalid_state_id(state_id=state_id)
        except InvalidDateFormat:
            presenter.raise_invalid_date_format()

    def state_get_cumulative_report(self, state_id: int, till_date: datetime.date):

        state_dto = self.get_state_details(state_id=state_id)
        self.validate_date_format(date=till_date)

        district_dtos = self.storage.get_districts_for_state(state_id)
        district_ids = [district.district_id for district in district_dtos]
        report_dtos = self.storage.get_cumulative_report_for_districts(
            district_ids=district_ids, till_date=till_date)

        self._initialize_report_stats()
        district_report_dtos = self._get_report_metrics(report_dtos=report_dtos)
        return self._convert_complete_state_cumulative_report_dto(state_dto,
            district_report_dtos, district_dtos)

    def _get_report_metrics(self, report_dtos: List[DistrictReportDto]):

        reports = []
        for report in report_dtos:
            district_report_dto = \
                self._convert_to_district_report_dto(report)
            reports.append(district_report_dto)
        return reports

    def _convert_to_district_report_dto(self, report: DistrictReportDto):

        district_id = report.district_id
        total_confirmed, total_recovered, total_deaths = \
                self.extract_report(report_dto=report)
        active_cases = total_confirmed - (total_recovered + total_deaths)

        self._add_report_stat_details(total_confirmed,
                    total_recovered, total_deaths, active_cases)

        district_report_dto = DistrictTotalReportDto(
                district_id=district_id,
                total_confirmed=total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths,
                active_cases=active_cases
            )
        return district_report_dto

    def _initialize_report_stats(self):

        self.total_confirmed = 0
        self.total_recovered = 0
        self.total_deaths = 0
        self.active_cases = 0

    def _add_report_stat_details(self, total_confirmed: int,
            total_recovered: int, total_deaths: int, active_cases: int):

        self.total_confirmed += total_confirmed
        self.total_recovered += total_recovered
        self.total_deaths += total_deaths
        self.active_cases += active_cases

    def _convert_complete_state_cumulative_report_dto(self, 
            state_dto, district_report_dtos, districts):

        state_cumulative_report_dto = TotalReportDto(
            total_confirmed=self.total_confirmed,
            total_recovered=self.total_recovered,
            total_deaths=self.total_deaths,
            active_cases=self.active_cases
        )

        state_cumulative_report_dto = CompleteStateCumulativeReportDto(
            state=state_dto,
            districts=districts,
            district_reports=district_report_dtos,
            state_cumulative_report=state_cumulative_report_dto
        )
        return state_cumulative_report_dto

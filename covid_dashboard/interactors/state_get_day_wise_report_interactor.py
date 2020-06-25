import datetime
from typing import List
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.interactors.mixins.extract_report \
    import ExtractReport
from covid_dashboard.interactors.mixins.validations import ValidationMixin
from covid_dashboard.interactors.storages.dtos \
    import DayReportDto, DayWiseReportDto
from covid_dashboard.exceptions.exceptions import *


class StateGetDaywiseReportInteractor:

    def __init__(self, storage: StateStorageInterface):

        self.storage = storage


    def state_get_day_wise_report_wrapper(self,
            presenter=PresenterInterface, state_id=1):
        try:
            day_wise_report_dtos = self.state_get_day_wise_report(state_id)
            response = \
                presenter.resonse_state_day_wise_report(
                    day_wise_report_dtos=day_wise_report_dtos)
            return response
        except InvalidStateId:
            raise presenter.raise_invalid_state_id(state_id=state_id)

    def state_get_day_wise_report(self, state_id: int):

        self.storage.check_state_id_is_valid(state_id)
        initial_date, final_date = self.storage.get_initial_and_final_dates()
        daily_report_dtos = self.storage.state_get_day_wise_report(
            state_id=state_id)
        day_wise_report_dtos = \
            self._get_day_wise_report_from_daily_report_list(
                daily_report_dtos, initial_date, final_date)
        return day_wise_report_dtos


    def _get_day_wise_report_from_daily_report_list(self,
            daily_report_dtos: List[DayReportDto], initial_date, final_date):

        index = 0
        date = initial_date
        day_wise_report_dtos = []
        report, index = self._get_next_report(daily_report_dtos, index)
        total_confirmed, total_recovered, total_deaths, total_active_cases = \
            0, 0, 0, 0
        while date <= final_date:
            confirmed, recovered, deaths = 0, 0, 0
            if report and report.date == date:
                confirmed, recovered, deaths = self._extract_report(report)
                report, index = self._get_next_report(daily_report_dtos, index) 
            active_cases = confirmed - (recovered + deaths)
            total_confirmed += confirmed
            total_recovered += recovered
            total_deaths += deaths
            total_active_cases += active_cases
            day_wise_report_dtos.append(
                self._convert_to_day_wise_report(date, total_confirmed,
                    total_recovered, total_deaths, total_active_cases)
            )
            date = self._get_next_day(date)
        return day_wise_report_dtos

    def _convert_to_day_wise_report(self, date, total_confirmed: int, \
            total_recovered: int, total_deaths: int, active_cases: int):
        return(
            DayWiseReportDto(
                date=date,
                total_confirmed=total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths,
                active_cases=active_cases
            )
        )
        
    def _extract_report(self, day_report: DayReportDto):
        total_confirmed = day_report.total_confirmed
        total_recovered = day_report.total_recovered
        total_deaths = day_report.total_deaths
        return total_confirmed, total_recovered, total_deaths

    def _get_next_day(self, date):
        timedelta = datetime.timedelta(days=1)
        next_day = date + timedelta
        return next_day

    def _get_next_report(self, reports, index):

        if index < len(reports):
            return reports[index], index + 1
        return None, index + 1
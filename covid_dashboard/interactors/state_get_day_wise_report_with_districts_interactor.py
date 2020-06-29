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
    import DistrictDto, DayReportDto, DistrictDayReportDto, \
        DistrictDayWiseReportDto, DayWiseReportDto
from covid_dashboard.interactors.mixins.validations import ValidationMixin
from covid_dashboard.exceptions.exceptions import InvalidStateId


class StateGetDayWiseReportWithDistrictsInteractor(ValidationMixin):

    def __init__(self, storage: StateStorageInterface):

        self.storage = storage

    def state_get_day_wise_report_with_districts_wrapper(self, 
            presenter: PresenterInterface, state_id=1):

        try:
            state_dto, all_district_reports = \
                self.state_get_day_wise_report_with_districts(
                    state_id=state_id)
            response = presenter.response_state_day_wise_report_with_districts(
                state_dto, all_district_reports)
            return response
        except InvalidStateId:
            presenter.raise_invalid_state_id(state_id=state_id)

    def state_get_day_wise_report_with_districts(self, state_id: int):

        state_dto = self.get_state_details(state_id=state_id)
        district_dtos = self.storage.get_districts_for_state(state_id)
        district_ids = [district.district_id for district in district_dtos]
        day_report_dtos = self.storage.get_day_wise_report_for_distrcts(
            district_ids=district_ids)

        all_district_reports = \
            self._convert_to_district_day_wise_reports(
                district_dtos=district_dtos, day_report_dtos=day_report_dtos)
        return state_dto, all_district_reports


    def _convert_to_district_day_wise_reports(self,
            district_dtos: DistrictDto, day_report_dtos: DistrictDayReportDto):

        all_district_reports = []
        initial_date, final_date = self.storage.get_initial_and_final_dates()
        for district_dto in district_dtos:
            reports = []
            date = initial_date
            total_confirmed, total_recovered, total_deaths, total_active_cases = \
                0, 0, 0, 0
            for district_day_report_dto in day_report_dtos:
                # confirmed, recovered, deaths = 0, 0, 0
                if district_dto.district_id == district_day_report_dto.district_id:
                    if date != district_day_report_dto.date:
                        previous_report = self._get_previous_report(reports)
                        missing_reports, date = \
                            self._missing_day_report_of_district(
                                district_dto, district_day_report_dto.date,
                                    date, previous_report)
                        reports.extend(missing_reports)
                    day_report_dto, total_confirmed, total_recovered, \
                        total_deaths, total_active_cases = \
                            self._get_day_wise_report(district_day_report_dto,
                        total_confirmed, total_recovered, total_deaths,
                        total_active_cases)
                    reports.append(day_report_dto)
                    date = self._get_next_day(date)

            if date <= final_date:
                print(date)
                expected_date = self._get_next_day(final_date)
                previous_report = self._get_previous_report(reports)
                missing_reports, date = \
                    self._missing_day_report_of_district(
                        district_dto, expected_date, date, previous_report)
                reports.extend(missing_reports)

            all_district_reports.append(
                self._convert_to_district_day_wise_report(district_dto, reports))
        return all_district_reports

    def _convert_to_district_day_wise_report(self,
            district_dto, reports) -> DistrictDayWiseReportDto:
        return(
            DistrictDayWiseReportDto(
                district_id=district_dto.district_id,
                district_name=district_dto.district_name,
                day_wise_reports=reports
            )
        )

    def _missing_day_report_of_district(self, district_dto: DistrictDto,
            expected_date, date, previous_report):
        reports = []
        confirmed, recovered, deaths = self._extract_report(previous_report)
        active_cases = confirmed - (recovered + deaths)
        while date < expected_date:
            print(district_dto.district_id, date)
            day_report_dto = \
            self._convert_to_day_wise_report(date, confirmed,
                recovered, deaths, active_cases)
            reports.append(day_report_dto)
            date = self._get_next_day(date)
        return reports, date

    def _extract_report(self, day_report: DayReportDto):
        total_confirmed = day_report.total_confirmed
        total_recovered = day_report.total_recovered
        total_deaths = day_report.total_deaths
        return total_confirmed, total_recovered, total_deaths

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

    def _get_day_wise_report(self, district_day_report_dto,
            total_confirmed: int, total_recovered: int, total_deaths: int,
            total_active_cases: int):
        confirmed, recovered, deaths = self._extract_report(district_day_report_dto)
        active_cases = confirmed - (recovered + deaths)
        total_confirmed += confirmed
        total_recovered += recovered
        total_deaths += deaths
        total_active_cases += active_cases
        date = district_day_report_dto.date
        day_report_dto = \
            self._convert_to_day_wise_report(date, total_confirmed,
                total_recovered, total_deaths, total_active_cases)
        return day_report_dto, total_confirmed, total_recovered, \
            total_deaths, total_active_cases

    def _get_next_day(self, date):
        timedelta = datetime.timedelta(days=1)
        next_day = date + timedelta
        return next_day

    def _get_previous_report(self, reports):
        some_day = datetime.date.today()
        last = -1
        if len(reports):
            return reports[last]
        return(
            DayWiseReportDto(
                date=some_day,
                total_confirmed=0,
                total_recovered=0,
                total_deaths=0,
                active_cases=0
            )
        )
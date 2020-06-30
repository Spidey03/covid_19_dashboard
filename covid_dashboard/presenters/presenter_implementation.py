from typing import List
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden
from covid_dashboard.constants.exception_messages import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.interactors.presenters.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def _convert_date(self, date):
        return str(date.strftime('%d-%b-%Y'))
        # return str(cumulative_report.date.strftime('%d-%b-%Y'))

    def raise_invalid_user_name(self):
        raise NotFound(*INVALID_USERNAME)

    def raise_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)

    def login_response(self, user_token_dto):
        user_login_response = {
            "user_id": user_token_dto.user_id,
            "access_token": user_token_dto.access_token,
            "refresh_token": user_token_dto.refresh_token,
            "expires_in": user_token_dto.expires_in
        }
        return user_login_response

    def raise_invalid_state_id(self, state_id: int):
        raise BadRequest(*INVALID_STATE_ID)

    def raise_invalid_date_format(self):
        raise BadRequest(*INVALID_DATE_FORMAT)

    def response_state_cumulative_report(self, 
            state_cumulative_report_dto: CompleteStateCumulativeReportDto):
        state = state_cumulative_report_dto.state
        district_dtos_list = state_cumulative_report_dto.districts
        district_report_dto_list = state_cumulative_report_dto.district_reports
        state_report = state_cumulative_report_dto.state_cumulative_report

        distri_report_list = \
            self._convert_district_dto_list(
                district_report_dto_list, district_dtos_list)
        response = {
            "state_name": state.state_name,
            "districts": distri_report_list,
            "total_cases":state_report.total_confirmed,
            "total_recovered_cases":state_report.total_recovered,
            "total_deaths":state_report.total_deaths,
            "active_cases":state_report.active_cases,
        }
        return response

    def _convert_district_dto_list(self, district_report_dto_list, district_dto_list):

        district_report_list = []
        for district_report_dto in district_report_dto_list:
            for district in district_dto_list:
                if district.district_id == district_report_dto.district_id:
                    district_name=district.district_name
                    break
            district_report_list.append({
                "district_name":district_name,
                "total_cases":district_report_dto.total_confirmed,
                "total_recovered_cases":district_report_dto.total_recovered,
                "total_deaths":district_report_dto.total_deaths,
                "active_cases":district_report_dto.active_cases,
            })
        return district_report_list

    def resonse_state_day_wise_report(self,
            day_wise_report_dtos: List[DayWiseReportDto]):

        day_wise_report_list = []
        for day_wise_report_dto in day_wise_report_dtos:
            day_wise_report_list.append({
                "date":self._convert_date(day_wise_report_dto.date),
                "total_cases": day_wise_report_dto.total_confirmed,
                "total_recovered_cases": day_wise_report_dto.total_recovered,
                "total_deaths": day_wise_report_dto.total_deaths,
                "active_cases": day_wise_report_dto.active_cases
            })
        return {"daily_cumulative":day_wise_report_list}

    def response_state_day_wise_report_with_districts(self, state_dto: StateDto,
            all_district_reports: List[DistrictDayWiseReportDto]):

        districts = []
        for district_day_wise_report_dto in all_district_reports:
            district_reports = []
            for report in district_day_wise_report_dto.day_wise_reports:
                district_reports.append(self._convert_to_day_report(report))
            districts.append({
                "district_id": district_day_wise_report_dto.district_id,
                "district_name": district_day_wise_report_dto.district_name,
                "daily_cumulative":district_reports
            })
        return({
            "state_name": state_dto.state_name,
            "districts": districts
        })

    def _convert_to_day_report(self, report: DayWiseReportDto):
        return({
            "date": self._convert_date(report.date),
            "total_cases": report.total_confirmed,
            "total_recovered_cases": report.total_recovered,
            "total_deaths": report.total_deaths,
            "active_cases": report.active_cases
        })

    def response_state_day_report(self,
            state_day_report_dto: StateDayReportDto):

        response = {
            "state_name":state_day_report_dto.state_name,
            "total_cases": state_day_report_dto.total_confirmed,
            "total_recovered_cases": state_day_report_dto.total_recovered,
            "total_deaths": state_day_report_dto.total_deaths,
            "districts": self._convert_to_district_reports(
                state_day_report_dto.district_reports)
        }
        return response

    def _convert_to_district_reports(self, district_reports):

        district_report_list = []
        for report in district_reports:
            district_report_list.append({
                "district_id": report.district_id,
                "total_cases": report.total_confirmed,
                "total_recovered_cases": report.total_recovered,
                "total_deaths": report.total_deaths,
            })
        return district_report_list

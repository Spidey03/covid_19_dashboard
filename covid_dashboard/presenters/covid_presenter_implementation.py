from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto)
from covid_dashboard.constants.exception_messages import INVALID_USERNAME, INVALID_PASSWORD
from covid_dashboard.exceptions.exceptions\
    import (InvalidStateId, InvalidDistrictId,
            InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId, InvalidStatsDetails, StatNotFound,
            DetailsAlreadyExist, InvalidDate)



class PresenterImplementation(PresenterInterface):

    def _convert_date(self, date):
        return str(date.strftime('%d-%b-%Y'))
        # return str(cumulative_report.date.strftime('%d-%b-%Y'))

    def get_response_login_user(self, tokens_dto: UserAuthTokensDTO):

        response = {
            "user_id":tokens_dto.user_id,
            "access_token":tokens_dto.access_token,
            "refresh_token":tokens_dto.refresh_token,
            "expires_in":tokens_dto.expires_in
        }
        return response


    def get_response_for_state_wise_daily_report(
            self, daily_state_report_dto: StateDto):
        pass


    def get_response_for_state_wise_cumulative_report(
            self, cumulative_state_report_dto: DistrictDto):
        stats = cumulative_state_report_dto.stats
        district_stats = []
        total_cases, total_deaths, total_recovered_cases, active_cases = \
            0,0,0,0
        for stat in stats:
            district ={
                "district_id":stat.district_id,
                "district_name":stat.district_name,
                # "date":stat.date,
                "total_cases":stat.total_cases,
                "total_deaths":stat.total_deaths,
                "total_recovered_cases":stat.total_recovered_cases,
                "active_cases":stat.active_cases
            }
            total_cases += stat.total_cases
            total_deaths += stat.total_deaths
            total_recovered_cases += stat.total_recovered_cases
            active_cases += stat.active_cases
            
            district_stats.append(district)
        state_stats={
            # "state_id":cumulative_state_report_dto.state_id,
            "state_name":cumulative_state_report_dto.state_name,
            "districts":district_stats,
            "total_cases":total_cases,
            "total_deaths":total_deaths,
            "total_recovered_cases":total_recovered_cases,
            "active_cases":active_cases
        }
        return state_stats


    def get_daily_cumulative_report_response(self,
            daily_cumulative_report_dto: DailyCumulativeReport):
    
        daily_cumulative_response = []
        reports = daily_cumulative_report_dto.report
        for cumulative_report in reports:
            report = {
                "date":self._convert_date(cumulative_report.date),
                "total_cases":cumulative_report.total_cases,
                "total_deaths":cumulative_report.total_deaths,
                "total_recovered_cases":cumulative_report.total_recovered_cases,
                'active_cases':cumulative_report.active_cases
            }
            daily_cumulative_response.append(report)
        response = {
            'daily_cumulative':daily_cumulative_response
        }
        return response


    def raiseinvalidusername(self):
        raise NotFound(*INVALID_USERNAME)


    def raiseinvalidpassword(self):
        raise NotFound(*INVALID_PASSWORD)


    def get_district_daily_cumulative_report_response(self,
            list_district_daily_cumulative):
        state_name = list_district_daily_cumulative.state_name
        districts = list_district_daily_cumulative.districts
        
        list_of_districts_reports = \
            self._convert_districts_report_to_response(districts)
        response = {
            "state_name":state_name,
            "districts":list_of_districts_reports
        }
        return response


    def _convert_districts_report_to_response(self, districts):
        list_of_districts_reports = []
        for district in districts:
            district_id = district.district_id
            district_name = district.district_name
            report = district.report
            district_report_list = self._get_convert_report(report)
            district_report = {
                "district_id":district_id,
            	"district_name":district_name,
            	"daily_cumulative":district_report_list
            }
            list_of_districts_reports.append(district_report)
        return list_of_districts_reports
	
	
    def _get_convert_district_report(self, reports):
        district_report_list = []
        for report in reports:
            district_report = self._conver_to_cumulative_report(report)
            district_report_list.append(district_report)
        return district_report_list
    
    def _get_convert_report(self, reports):
        report_list = []
        for report in reports:
            report_data = self._conver_to_cumulative_report(report)
            report_list.append(report_data)
        return report_list

    def _conver_to_cumulative_report(self, report):
        report_dict = {
            "date": self._convert_date(report.date),
            "total_cases": report.total_cases,
            "total_deaths": report.total_deaths,
            "total_recovered_cases": report.total_recovered_cases,
            "active_cases": report.active_cases
        }
        return report_dict

    def raise_invalid_details_for_total_confirmed(self):
        raise InvalidDetailsForTotalConfirmed

    def raise_invalid_details_for_total_deaths(self):
        raise InvalidDetailsForTotalDeaths


    def raise_invalid_details_for_total_recovered(self):
        raise InvalidDetailsForTotalRecovered


    def raise_invalid_details_for_mandal_id(self):
        raise InvalidMandalId

    def raise_invalid_stats_details(self):
        raise InvalidStatsDetails

    def raise_stat_not_found(self):
        raise StatNotFound


    def raise_details_already_exist(self):
        raise DetailsAlreadyExist


    def get_response_for_report_of_state_for_date(self, report):
        districts = report.districts
        response = {
            "state_name": report.state_name,
            "districts":self._get_district_report_of_a_date(districts),
            "total_cases": report.total_cases,
            "total_recovered_cases": report.total_recovered_cases,
            "total_deaths": report.total_deaths    
        }
        return response
    
    def _get_district_report_of_a_date(self, districts):
        reports = []
        for district in districts:
            district = {
                "district_id":district.district_id,
                "district_name":district.district_name,
                "total_cases":district.total_cases,
                "total_recovered_cases":district.total_recovered_cases,
                "total_deaths":district.total_deaths
            }
            reports.append(district)
        return reports

    def raise_invalid_date(self):
        raise InvalidDate


    def get_response_for_state_wise_daily_cases_report(self,
            daily_state_report_dto):
        reports = []
        for report in daily_state_report_dto:
            reports.append({
                'date':self._convert_date(report.date),
                'total_cases':report.total_cases,
                'total_deaths':report.total_deaths,
                'total_recovered_cases':report.total_recovered_cases,
                'active_cases':report.active_cases
            })
        return reports


    def get_response_for_district_cumulative_report(self, report):
        response = {
            # "district_id":report.district_id,
            "district_name":report.district_name,
            "mandals":self._convert_to_mandal_cumulative_report_for_district(report.mandals),
            "total_cases":report.total_cases,
            "total_recovered_cases":report.total_recovered_cases,
            "total_deaths":report.total_deaths,
            "active_cases":report.active_cases
        }
        return response

    def _convert_to_mandal_cumulative_report_for_district(self, mandals):
        mandal_reports = []
        for mandal in mandals:
            mandal_reports.append(
                {
                    "mandal_id":mandal.mandal_id,
                    "mandal_name": mandal.mandal_name,
                    "total_cases": mandal.total_cases,
                    "total_recovered_cases":mandal.total_recovered_cases,
                    "total_deaths":mandal.total_deaths,
                    "active_cases":mandal.active_cases
                }
            )
        return mandal_reports
    
    
    def get_response_for_daily_cumulative_report_for_district(self,
        district_report):
        response = []
        reports = district_report.report
        for report in reports:
            response.append(
                {
                    "date":self._convert_date(report.date),
                    "total_cases":report.total_cases,
                    "total_deaths":report.total_deaths,
                    "total_recovered_cases":report.total_recovered_cases,
                    "active_cases":report.active_cases
                }
            )
        return ({
            "daily_cumulative":response
        })
    
    def raise_invalid_district_id(self):
        raise InvalidDistrictId


    def get_response_for_daily_cumulative_report_of_mandals_for_district(self,
            district_report):
        district_name = district_report.district_name
        mandals = district_report.mandals

        mandal_reports = \
            self._convert_mandal_reports(mandals)
        response = {
            "district_name":district_name,
            "mandals":mandal_reports
        }
        return response

    def _convert_mandal_reports(self, mandals):
        reports_list = []
        for mandal in mandals:
            report = mandal.report
            mandal_report_list = self._get_convert_report(report)
            mandal_report = {
                'mandal_id':mandal.mandal_id,
                'mandal_name':mandal.mandal_name,
                'daily_cumulative':mandal_report_list
            }
            reports_list.append(mandal_report)
        return reports_list


    def get_response_district_report_of_specific_day(self, report):
        mandals = self._convert_to_mandal_specific_day(report.mandals)
        return({
            "district_name":report.district_name,
            "mandals":mandals,
            "total_cases":report.total_cases,
            "total_deaths":report.total_deaths,
            "total_recovered_cases":report.total_recovered_cases
        })


    def _convert_to_mandal_specific_day(self, mandals):
        mandal_reports = []
        for mandal in mandals:
            mandal_reports.append({
                "mandal_id":mandal.mandal_id,
                "mandal_name":mandal.mandal_name,
                "total_cases":mandal.total_cases,
                "total_deaths":mandal.total_deaths,
                "total_recovered_cases":mandal.total_recovered_cases
            })
        return mandal_reports
        
    def get_response_for_get_statistics(self, mandal_report):
        return(
            {
                "mandal_id":mandal_report.mandal_id,
                "mandal_name":mandal_report.mandal_name,
                "reports":self._convert_to_mandal_reports(mandal_report.reports)
            }
        )
    
    def _convert_to_mandal_reports(self, reports):
        mandal_reports = []
        for report in reports:
            mandal_reports.append(
                {
                    "date":self._convert_date(report.date),
                    "total_cases":report.total_cases,
                    "total_deaths":report.total_deaths,
                    "total_recovered_cases":report.total_recovered_cases
                }
            )
        return mandal_reports

    def get_response_get_day_wise_district_details(self, district_report_list):
        response = []
        for report in district_report_list:
            report_dict = {
                "date":self._convert_date(report.date),
                "total_cases":report.total_cases,
                "total_recovered_cases":report.total_recovered_cases,
                "total_deaths":report.total_deaths,
                "active_cases":report.active_cases
            }
            response.append(report_dict)
        return response

    def get_response_get_day_wise_mandal_details(self, district_report_dict):
        response = self.get_response_for_daily_cumulative_report_of_mandals_for_district(
                district_report_dict)
        return response


    def raise_user_not_admin(self):
        pass
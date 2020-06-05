from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos\
    import (ListMandalDailyCumulativeReportDto,
            MandalCumulativeReportOnSpecificDayDto,
            CumulativeReportOnSpecificDay
           )


class GetDailyCumulativeReportOfMandalsForDistrict:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_daily_cumulative_report_of_mandals_for_district(self, district_id):
        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()

        district_report_dict = self.storage.\
            get_daily_cumulative_report_of_mandals_for_district(district_id)

        # Business Logic
        mandal_wise_daily_cumulative_report_dto = \
            self._convert_to_list_mandal_daily_cumulative(district_report_dict)

        response = self.presenter.\
            get_response_for_daily_cumulative_report_of_mandals_for_district(
                mandal_wise_daily_cumulative_report_dto
            )
        return response


    def _convert_to_list_mandal_daily_cumulative(self,
            district_report_dict):
        mandals_daily_cumulative_report_list = \
            self._get_mandal_daily_cumulative_report_list(
                district_report_dict['reports'],
                district_report_dict['mandals']
            )

        list_mandal_daily_cumulative = ListMandalDailyCumulativeReportDto(
            district_name=district_report_dict['district_name'],
            mandals=mandals_daily_cumulative_report_list
        )
        return list_mandal_daily_cumulative


    def _get_mandal_daily_cumulative_report_list(self, reports_dict,
            mandals_details):
        list_mandals_report = []
        for mandal_id, mandal_daily_reports in reports_dict.items():
            mandal_name=mandals_details[mandal_id]['mandal_name']
            mandal_report_dto = MandalCumulativeReportOnSpecificDayDto(
                mandal_id=mandal_id,
                mandal_name=mandal_name,
                report = self._get_reports_for_mandal(mandal_daily_reports)
            )
            list_mandals_report.append(mandal_report_dto)
        return list_mandals_report

    def _get_reports_for_mandal(self, mandal_daily_reports):
        index = 0
        daily_cumulative_report_list = []
        date = mandal_daily_reports[index]['date']
        report, index = \
            self._get_next_report(mandal_daily_reports, index)
        total_cases, total_deaths, total_recovered, active_cases = \
                0, 0, 0, 0

        while report:
            today_cases, today_deaths, today_recovered, today_active_cases = \
                0, 0, 0, 0
            if date == report['date']:
                today_cases, today_deaths, today_recovered = \
                    self._get_stat_details(report)
                today_active_cases = report['active_cases']
                report, index = \
                    self._get_next_report(mandal_daily_reports, index)

            total_cases += today_cases
            total_deaths += today_deaths
            total_recovered += today_recovered
            today_active_cases = today_cases - (today_recovered + today_deaths)
            active_cases += today_active_cases

            daily_cumulative_report_dto = CumulativeReportOnSpecificDay(
                date=date,
                total_cases=total_cases,
                total_deaths=total_deaths,
                total_recovered_cases=total_recovered,
                active_cases=active_cases
            )
            daily_cumulative_report_list.append(daily_cumulative_report_dto)
            date = self._get_next_day(date)
            
        return daily_cumulative_report_list

    def _get_next_report(self, mandal_daily_reports, index):
        if index < len(mandal_daily_reports):
            report = mandal_daily_reports[index]
        else:
            report = None
        return report, index+1

    def _get_next_day(self, date):
        import datetime
        timedelata = datetime.timedelta(days=1)
        return date + timedelata

    def _get_stat_details(self, stat):
        today_cases = stat['total_cases']
        today_deaths= stat['total_deaths']
        today_recovered_cases = stat['total_recovered_cases']
        return today_cases, today_deaths, today_recovered_cases

from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import *



class GetDayWiseMandalDetails:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_day_wise_mandal_details(self, district_id):

        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()

        district_report_dict = self.storage.get_day_wise_mandal_details(
            district_id)

        mandal_day_wise_report_dto = \
            self._convert_to_list_mandal_daily_cumulative(
                district_report_dict)

        response = self.presenter.\
            get_response_get_day_wise_mandal_details(
                mandal_day_wise_report_dto)
        return response


    def _convert_to_list_mandal_daily_cumulative(self,
            district_report_dict):
        mandals = self._get_mandal_daily_cumulative_report(
            district_report_dict['reports'], district_report_dict['mandals'])

        list_mandal_daily_cumulative = ListMandalDailyCumulativeReportDto(
            district_name=district_report_dict['district_name'],
            mandals=mandals
        )
        return list_mandal_daily_cumulative


    def _get_mandal_daily_cumulative_report(self, reports, mandals):
        list_mandals_report = []
        for mandal_id, mandal_daily_reports in reports.items():
            mandal_name=mandals[mandal_id]['mandal_name']
            mandal_report_dto = MandalCumulativeReportOnSpecificDayDto(
                mandal_id=mandal_id,
                mandal_name=mandal_name,
                report = self._get_reports_for_mandal(mandal_daily_reports)
            )
            list_mandals_report.append(mandal_report_dto)
        return list_mandals_report

    def _get_reports_for_mandal(self, mandal_daily_reports):
        daily_cumulative_report_list = []
        index = 0
        date, final_date = self._get_initial_and_final_dates(
            mandal_daily_reports)
        date = mandal_daily_reports[index]['date']
        report, index = self._get_next_report(mandal_daily_reports, index)
        while date <= final_date:
            total_cases, total_deaths, total_recovered, active_cases = \
                0, 0, 0, 0
            if date == report['date']:
                total_cases, total_deaths, total_recovered = \
                    self._get_stat_details(report)
                active_cases = report['active_cases']
                report, index = \
                    self._get_next_report(mandal_daily_reports, index)

            daily_cumulative_report_dto = CumulativeReportOnSpecificDay(
                date=date,
                total_cases=total_cases,
                total_deaths=total_deaths,
                active_cases=active_cases,
                total_recovered_cases=total_recovered
            )
            date = self._get_next_day(date)
            daily_cumulative_report_list.append(daily_cumulative_report_dto)

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

    def _get_initial_and_final_dates(self, stats):
        initial, final = 0, len(stats)-1
        initial_date = stats[initial]['date']
        final_date = stats[final]['date']
        return initial_date, final_date

    def _get_stat_details(self, stat):
        today_cases = stat['total_cases']
        today_deaths= stat['total_deaths']
        today_recovered_cases = stat['total_recovered_cases']
        return today_cases, today_deaths, today_recovered_cases

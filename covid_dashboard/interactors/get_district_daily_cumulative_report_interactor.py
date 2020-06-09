from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.storages.dtos\
    import (ListDistrictDailyCumulativeReport, CumulativeReportOnSpecificDay,
    DistrictCumulativeReportOnSpecificDay)
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId


class GetDistrictDailyCumulativeReport:

    def __init__(self,
            storage=StateStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_district_daily_cumulative_report(self):

        district_wise_daily_cumulative_report_dict = \
            self.storage.get_district_daily_cumulative_report()

        # Business Logic
        list_district_daily_cumulative = \
            self._convert_to_list_district_daily_cumulative(
                district_wise_daily_cumulative_report_dict
            )
        response = self.presenter.get_district_daily_cumulative_report_response(
            list_district_daily_cumulative)
        return response
        # return list_district_daily_cumulative


    def _convert_to_list_district_daily_cumulative(self,
            reports_dict):
        districts = self._get_district_daily_cumulative_report(
            reports_dict['reports'], reports_dict['districts'])

        list_district_daily_cumulative = ListDistrictDailyCumulativeReport(
            state_name=reports_dict['state_name'],
            districts=districts
        )
        return list_district_daily_cumulative


    def _get_district_daily_cumulative_report(self, reports, districts):
        list_districs_report = []
        for district_id, district_report in reports.items():
            district_name=districts[district_id]['district_name']
            district_report = DistrictCumulativeReportOnSpecificDay(
                district_id=district_id,
                district_name=district_name,
                report = self._get_report_for_district(district_report)
            )
            list_districs_report.append(district_report)
        return list_districs_report

    def _get_report_for_district(self, district_report_list):
        index = 0
        daily_cumulative_report_list = []
        initial_date, final_date = self._get_initial_and_final_date()
        date = initial_date
        report, index = self._get_next_report(district_report_list, index)
        daily_cumulative_report_list = []
        total_cases, total_deaths, total_recovered, active_cases = \
                0, 0, 0, 0
        while date <= final_date:
            today_cases, today_deaths, today_recovered, today_active_cases = \
                0, 0, 0, 0
            if date == report['date']:
                today_cases, today_deaths, today_recovered = \
                    self._get_stat_details(report)
                today_active_cases = today_cases - \
                    (today_deaths + today_recovered)
                report, index = self._get_next_report(district_report_list, index)
            total_cases += today_cases
            total_deaths += today_deaths
            total_recovered += today_recovered
            active_cases += today_active_cases
            daily_cumulative_report_dto = CumulativeReportOnSpecificDay(
                date=date,
                total_cases=total_cases,
                total_deaths=total_deaths,
                total_recovered_cases=total_recovered,
                active_cases=active_cases
            )
            date = self._get_next_day(date)
            daily_cumulative_report_list.append(daily_cumulative_report_dto)
        return daily_cumulative_report_list

    def _get_initial_and_final_date(self):
        dates = self.storage._get_initial_and_final_date()
        return dates[0], dates[1]

    def _get_next_day(self, date):
        import datetime
        timedelata = datetime.timedelta(days=1)
        return date + timedelata

    def _get_next_report(self, reports, index):
        if index < len(reports):
            report = reports[index]
        else:
            report = {'date':None}
        return report, index+1

    def _get_stat_details(self, stat):
        today_cases = stat['total_cases']
        today_deaths= stat['total_deaths']
        today_recovered_cases = stat['total_recovered_cases']
        return today_cases, today_deaths, today_recovered_cases
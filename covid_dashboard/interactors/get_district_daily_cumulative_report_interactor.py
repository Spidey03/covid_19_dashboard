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

    def _get_report_for_district(self, district_report):
        import datetime
        daily_cumulative_report_list = []
        first, next = 0, 1
        date = district_report[first]['date']
        report = district_report[first]
        get_next = False
        timedelta = datetime.timedelta(days=1)
        daily_cumulative_report_list = []
        while report:
            total_cases, total_deaths, total_recovered, active_cases = \
                0, 0, 0, 0
            if date == report['date']:
                total_cases, total_deaths, total_recovered, active_cases = \
                    report['total_cases'], report['total_deaths'],\
                    report['total_recovered_cases'], report['active_cases']
                get_next = True

            daily_cumulative_report_dto = CumulativeReportOnSpecificDay(
                date=report['date'],
                total_cases=report['total_cases'],
                total_deaths=report['total_deaths'],
                total_recovered_cases=report['total_recovered_cases'],
                active_cases=report['active_cases']
            )
            if get_next:
                if next < len(district_report):
                    report = district_report[next]
                    next += 1
                else:
                    break
                get_next = False
            date = date + timedelta
            daily_cumulative_report_list.append(daily_cumulative_report_dto)
        return daily_cumulative_report_list
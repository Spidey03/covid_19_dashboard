from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.storages.dtos\
    import (ListDistrictDailyCumulativeReport, CumulativeReportOnSpecificDay,
    DistrictCumulativeReportOnSpecificDay)
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId, InvalidDate


class GetDistrictReportOfSpecificDay:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_district_report_of_specific_day(self, district_id, date):
        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()
        try:
            self.storage.check_is_date_valid(date)
        except InvalidDate:
            self.presenter.raise_invalid_date()
        report = self.storage.get_district_report_of_specific_day(
            district_id=district_id, date=date)
        return self.presenter.get_response_district_report_of_specific_day(report)

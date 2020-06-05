from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions import InvalidDistrictId



class GetDailyCumulativeReportForDistrict:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_daily_cumulative_report_for_district(self, district_id: int):

        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()

        district_report = self.storage.get_daily_cumulative_report_for_district(
            district_id)
        response = self.presenter.\
            get_response_for_daily_cumulative_report_for_district(
                district_report)
        return response
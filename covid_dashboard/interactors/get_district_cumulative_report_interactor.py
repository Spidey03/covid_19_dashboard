from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId


class GetDistrictCumulativeReport:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_district_cumulative_report(self, till_date, district_id):
        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()

        report = self.storage.get_district_cumulative_report(
            till_date, district_id)

        response = self.presenter.get_response_for_district_cumulative_report(
            report)
        return response


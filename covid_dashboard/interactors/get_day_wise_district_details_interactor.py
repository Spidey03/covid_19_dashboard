from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions import InvalidDistrictId



class GetDayWiseDistrictDetails:

    def __init__(self,
            storage=DistrictStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_day_wise_district_details(self, district_id):

        try:
            self.storage.is_district_id_valid(district_id)
        except InvalidDistrictId:
            self.presenter.raise_invalid_district_id()

        district_report_list = self.storage.get_day_wise_district_details(
            district_id)

        response = self.presenter.\
            get_response_get_day_wise_district_details(district_report_list)
        return response
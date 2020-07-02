from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions \
    import InvalidMandalId, InvalidDetailsForTotalDeaths, \
        DetailsAlreadyExist, InvalidStatsDetails, \
        InvalidDetailsForTotalConfirmed, UserNotAdmin, \
        InvalidDetailsForTotalRecovered

from covid_dashboard.adapters.service_adapter import get_service_adapter


class AddNewStatistics:

    def __init__(self,
            storage=MandalStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def add_new_statistics(self, mandal_id: int, user_id: int,
            date, total_confirmed: int, total_deaths: int, total_recovered: int):
        
        try:
            self.storage.is_valid_mandal_id(mandal_id)
        except InvalidMandalId:
            self.presenter.raise_invalid_details_for_mandal_id()

        try:
            self.storage.is_valid_total_confirmed(total_confirmed)
        except InvalidDetailsForTotalConfirmed:
            self.presenter.raise_invalid_details_for_total_confirmed()

        try:
            self.storage.is_valid_total_deaths(total_deaths)
        except InvalidDetailsForTotalDeaths:
            self.presenter.raise_invalid_details_for_total_deaths()

        try:
            self.storage.is_valid_total_recovered(total_recovered)
        except InvalidDetailsForTotalRecovered:
            self.presenter.raise_invalid_details_for_total_recovered()

        try:
            self.storage.is_already_exist(mandal_id=mandal_id, date=date)
        except DetailsAlreadyExist:
            self.presenter.raise_details_already_exist()

        self._check_is_valid_user_admin(user_id)
        # try:
        #     self.storage.is_user_admin(user)
        # except UserNotAdmin:
        #     self.presenter.raise_user_not_admin()


        self.storage.add_new_statistics(mandal_id, total_confirmed,
            date, total_deaths, total_recovered
        )
        # try:
        #     self.storage.is_statistics_valid(total_confirmed, total_deaths, total_recovered)
        # except InvalidStatsDetails:
        #     self.presenter.raise_invalid_stats_details()


    def _check_is_valid_user_admin(self, user_id):

        service_adapter = get_service_adapter()

        user_details_dto = \
            service_adapter.auth_service.get_user_dto(user_id=user_id)

        is_user_admin = user_details_dto.is_admin
        is_invalid_user_admin = not is_user_admin

        if is_invalid_user_admin:
            self.presenter.raise_user_not_admin()

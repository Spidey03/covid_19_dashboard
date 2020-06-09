from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import (InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId, InvalidStatsDetails,
            StatNotFound, UserNotAdmin
           )


class UpdateStatistics:

    def __init__(self,
            storage=MandalStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def update_statistics(self, mandal_id: int, user, 
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
            self.storage.is_user_admin(user)
        except UserNotAdmin:
            self.presenter.raise_user_not_admin()
        # try:
        #     self.storage.is_statistics_valid(total_confirmed, total_deaths, total_recovered)
        # except InvalidStatsDetails:
        #     self.presenter.raise_invalid_stats_details()
        try:
            self.storage.update_statistics(mandal_id, total_confirmed,
                 date, total_deaths, total_recovered
            )
        except StatNotFound:
            self.presenter.raise_stat_not_found()
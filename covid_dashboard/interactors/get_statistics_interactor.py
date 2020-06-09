from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions import InvalidMandalId, UserNotAdmin

class GetStatistics:

    def __init__(self,
            storage=MandalStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_statistics(self, mandal_id: int, user):
        try:
            self.storage.is_user_admin(user)
        except UserNotAdmin:
            self.presenter.raise_user_not_admin()
        try:
            self.storage.is_valid_mandal_id(mandal_id)
        except InvalidMandalId:
            self.presenter.raise_invalid_details_for_mandal_id()
        report = self.storage.get_statistics(mandal_id)
        return self.presenter.get_response_for_get_statistics(report)
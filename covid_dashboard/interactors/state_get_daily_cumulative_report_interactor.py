from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId


class GetDailyCumulativeReport:

    def __init__(self,
            storage=StateStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_daily_cumulative_report(self):

        daily_cumulative_report_dto = \
            self.storage.get_daily_cumulative_report()

        response = self.presenter.get_daily_cumulative_report_response(
            daily_cumulative_report_dto)
        return response
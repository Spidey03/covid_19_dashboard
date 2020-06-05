from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId


class GetStateWiseDailyCasesReport:

    def __init__(self,
            storage=StateStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_state_wise_daily_cases_report(self):

        daily_state_report_dto = self.storage.\
            get_state_wise_daily_cases_report()
        response = self.presenter.\
            get_response_for_state_wise_daily_cases_report(daily_state_report_dto)
        return response
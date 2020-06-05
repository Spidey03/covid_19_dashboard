from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidDate



class GetReportOFStateForDate:

    def __init__(self,
            storage=StateStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_report_of_state_for_date(self, date):
        try:
            self.storage.check_is_date_valid(date)
        except InvalidDate:
            self.presenter.raise_invalid_date()
        report = self.storage.get_report_of_state_for_date(date)
        return self.presenter.get_response_for_report_of_state_for_date(report)
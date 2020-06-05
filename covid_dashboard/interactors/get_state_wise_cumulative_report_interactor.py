from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId, InvalidDate
from covid_dashboard.interactors.storages.dtos import StateStatsDtoWithMetrics


class GetStateWiseCumulativeReport:

    def __init__(self,
            storage=StateStorageInterface,
            presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_state_wise_cumulative_report(self, till_date):
        # try:
        #     self.storage.check_is_date_valid(till_date)
        # except InvalidDate:
        #     self.presenter.raise_invalid_date()
        cumulative_state_report_dto = self.storage.\
            get_state_wise_cumulative_report(till_date)

        # Business Logic
        
        state_stats_dto_with_metrics = \
            self._convert_to_state_stats_dto_with_metrics(
                cumulative_state_report_dto)
                
        response = self.presenter.\
            get_response_for_state_wise_cumulative_report(
                state_stats_dto_with_metrics)
        return response

    def _convert_to_state_stats_dto_with_metrics(self,
            cumulative_state_report_dto):
        stats = cumulative_state_report_dto.stats
        total_cases, total_deaths, total_recovered_cases, active_cases = \
            self._get_metrics(stats)

        state_stats_dto_with_metrics = \
            StateStatsDtoWithMetrics(
                state_id=cumulative_state_report_dto.state_id,
                state_name=cumulative_state_report_dto.state_name,
                stats=cumulative_state_report_dto.stats,
                total_cases=total_cases,
                total_deaths=total_deaths,
                total_recovered_cases=total_recovered_cases,
                active_cases=active_cases
            )
        return state_stats_dto_with_metrics
    
    
    def _get_metrics(self, stats):
        total_cases, total_deaths, total_recovered_cases, active_cases = \
            0,0,0,0
        for stat in stats:
            total_cases += stat.total_cases
            total_deaths += stat.total_deaths
            total_recovered_cases =+ stat.total_recovered_cases
            active_cases += stat.active_cases
    
        return total_cases, total_deaths, total_recovered_cases, active_cases
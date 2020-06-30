import pytest
import datetime
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos import DayReportDto, DistrictDayReportDto


class TestStateGetDayReportInteractor:

    @pytest.mark.django_db
    def test_get_day_report_for_state(self, states, districts, mandals, stats):

        # Arrange
        state_id = 1
        district_ids = [1,2]
        date = datetime.date(year=2020, month=5, day=27)
        expected_district_day_report_dtos = [
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=10,
                total_recovered=2,
                total_deaths=0,
                district_id=1
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=11,
                total_recovered=3,
                total_deaths=5,
                district_id=2
            )
        ]
        storage = StateStorageImplementation()

        # Act
        district_day_report_dtos = storage.get_day_report_districts(
            district_ids=district_ids, date=date)

        # Assert
        assert district_day_report_dtos == expected_district_day_report_dtos

    # def get_day_report_districts(self,
    #         district_ids: List[int], date) -> List[DistrictDayReportDto]:

    #     report_query_set = Stats.objects.values('mandal__district_id') \
    #                             .annotate(
    #                                 district_id = F('mandal__district_id'),
    #                                 total_confirmed=Sum('total_confirmed'),
    #                                 total_recovered=Sum('total_recovered'),
    #                                 total_deaths=Sum('total_deaths')
    #                             ).filter(
    #                                 mandal__district_id__in=district_ids,
    #                                 date=date
    #                             ).order_by('mandal__district_id')

    #     return self._convert_to_district_day_report_dtos(report_query_set)

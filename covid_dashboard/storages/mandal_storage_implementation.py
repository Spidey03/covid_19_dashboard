import datetime
from abc import ABC
from abc import abstractmethod
from typing import List
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.models\
    import State, District, Mandal, Stats, User
from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto,
            DailyCumulativeDistrictWise, DistrictDetails,
            DistrictReportForADate, StateReportForADate, Report,
            StateDailyReport, DistrictReportDto, MandalReportDto,
            DailyCumulativeMandalWiseReportDto, DistrictReportOfDay,
            MandalReportOfDay, Statistics, MandalStatistics)
from covid_dashboard.exceptions.exceptions\
    import (InvalidStateId, InvalidDistrictId,
            InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId, InvalidStatsDetails, StatNotFound,
            DetailsAlreadyExist, InvalidDate, UserNotAdmin)


class MandalStorageImplementation(MandalStorageInterface):

    def is_user_admin(self, user):
        if not user.is_superuser:
            raise UserNotAdmin

    def is_valid_total_confirmed(self, total_confirmed: int):
        is_valid = self._check_valid(total_confirmed)
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidDetailsForTotalConfirmed

    def is_valid_total_deaths(self, total_deaths: int):
        is_valid = self._check_valid(total_deaths)
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidDetailsForTotalDeaths

    def is_valid_total_recovered(self, total_recovered: int):
        is_valid = self._check_valid(total_recovered)
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidDetailsForTotalRecovered

    def is_valid_mandal_id(self, mandal_id: int):
        try:
            Mandal.objects.get(id=mandal_id)
        except Mandal.DoesNotExist:
            raise InvalidMandalId

    def check_is_date_valid(self, date):
        import datetime
        today = datetime.date.today()
        if date > today:
            raise InvalidDate

    def add_new_statistics(self, mandal_id: int, total_confirmed: int,
            date, total_deaths: int, total_recovered: int):
        Stats.objects.create(mandal_id=mandal_id,
            date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths,
            total_recovered=total_recovered)

    def update_statistics(self, mandal_id: int, total_confirmed: int,
            date, total_deaths: int, total_recovered: int):
        stat = Stats.objects.filter(mandal_id=mandal_id, date=date)
        if not stat:
            raise StatNotFound
        stat.update(
            total_confirmed=total_confirmed, total_deaths=total_deaths,
            total_recovered=total_recovered
        )



    def _check_valid(self, value: int):
        if value >= 0:
            return True
        return False

    def is_statistics_valid(self, total_confirmed: int, 
            total_deaths: int, total_recovered: int):
        if total_deaths + total_recovered > total_confirmed:
            raise InvalidStatsDetails

    def is_already_exist(self, mandal_id: int, date: int):
        stat = Stats.objects.filter(mandal_id=mandal_id, date=date)
        if stat:
            raise DetailsAlreadyExist

    def get_statistics(self, mandal_id):
        stats = Stats.objects.select_related('mandal')\
                    .filter(mandal_id=mandal_id)
        mandal_name = Mandal.objects.get(id=mandal_id).name
        reports = []
        for stat in stats:
            reports.append(
                Statistics(
                    date=stat.date,
                    total_cases=stat.total_confirmed,
                    total_deaths=stat.total_deaths,
                    total_recovered_cases=stat.total_recovered
                )
            )
        return (
            MandalStatistics(
                mandal_id=mandal_id,
                mandal_name=mandal_name,
                reports=reports
            )
        )
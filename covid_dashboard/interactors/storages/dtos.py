import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class StateDto:
    state_id: int
    state_name: str

@dataclass
class DistrictDto:
    district_id: int
    district_name: str


@dataclass
class DistrictReportDto:
    district_id: int
    total_confirmed: int
    total_recovered: int
    total_deaths: int

@dataclass
class DistrictTotalReportDto:
    district_id: int
    total_confirmed: int
    total_recovered: int
    total_deaths: int
    active_cases: int

@dataclass
class TotalReportDto:
    total_confirmed: int
    total_recovered: int
    total_deaths: int
    active_cases: int


@dataclass
class CompleteStateCumulativeReportDto:
    state: StateDto
    districts: List[DistrictDto]
    district_reports: List[DistrictTotalReportDto]
    state_cumulative_report: TotalReportDto

@dataclass
class DayReportDto:
    date: datetime.date
    total_confirmed: int
    total_recovered: int
    total_deaths: int

@dataclass
class DayWiseReportDto:
    date: datetime.date
    total_confirmed: int
    total_recovered: int
    total_deaths: int
    active_cases: int

@dataclass
class DistrictDayReportDto(DayReportDto):
    district_id: int

@dataclass
class DistrictDayWiseReportDto:
    district_id: int
    district_name: str
    day_wise_reports: List[DayWiseReportDto]

@dataclass
class StateDayReportDto:
    state_name: str
    district_reports: List[DistrictDayReportDto]
    total_confirmed: int
    total_recovered: int
    total_deaths: int

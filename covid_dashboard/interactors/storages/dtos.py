from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional
from collections import defaultdict


@dataclass
class MandalStatDto:
	mandal_id: int
	date: datetime.date
	total_cases: int
	total_deaths: int
	total_recovered_cases: int
	active_cases: int


@dataclass
class DistrictDto:
	district_id: int
	district_name: str
	stats: List[MandalStatDto]


@dataclass
class DistrictStatDto:
	district_id: int
	district_name: str
	date: datetime.date
	total_cases: int
	total_deaths: int
	total_recovered_cases: int
	active_cases: int


@dataclass
class StateDto:
	state_id: int
	state_name: str
	stats: List[DistrictStatDto]


@dataclass
class CumulativeReportOnSpecificDay:
    date: datetime.date
    total_cases: int
    total_deaths: int
    total_recovered_cases: int
    active_cases: int
                


@dataclass
class DailyCumulativeReport:
    report: List[CumulativeReportOnSpecificDay]
 
 
@dataclass
class StateStatsDtoWithMetrics(StateDto):
	total_cases: int
	total_deaths: int
	total_recovered_cases: int
	active_cases: int


@dataclass
class DistrictCumulativeReportOnSpecificDay:
	district_id: int
	district_name: str
	report: List[CumulativeReportOnSpecificDay]


@dataclass
class ListDistrictDailyCumulativeReport:
	state_name: str
	districts: List[DistrictCumulativeReportOnSpecificDay]
	

@dataclass
class DistrictDetails:
	district_id: int
	district_name: str

@dataclass
class DailyCumulativeDistrictWise:
	state_name: str
	districts: dict
	reports: List[defaultdict]




# MVP2

@dataclass
class DistrictReportForADate:
	district_id: int
	district_name: str
	total_cases: int
	total_recovered_cases: int
	total_deaths: int


@dataclass
class StateReportForADate:
	state_name: str
	districts: List[DistrictReportForADate]
	total_cases: int
	total_recovered_cases: int
	total_deaths: int


@dataclass
class Report:
	date: datetime.date
	total_cases: int
	total_recovered_cases: int
	total_deaths: int
	active_cases: int

@dataclass
class StateDailyReport:
	reports: List[Report]

@dataclass
class MandalReportDto:
	mandal_id: int
	mandal_name: str
	total_cases: int
	total_deaths: int
	total_recovered_cases: int
	active_cases: int


@dataclass
class DistrictReportDto:
	# district_id: int
	district_name: str
	mandals: List[MandalReportDto]
	total_cases: int
	total_deaths: int
	total_recovered_cases: int
	active_cases: int

@dataclass
class DailyCumulativeMandalWiseReportDto:
	district_name: str
	mandals: dict
	reports: List[defaultdict]


@dataclass
class MandalCumulativeReportOnSpecificDayDto:
	mandal_id: int
	mandal_name: str
	report: List[CumulativeReportOnSpecificDay]


@dataclass
class ListMandalDailyCumulativeReportDto:
	district_name: str
	mandals: List[MandalCumulativeReportOnSpecificDayDto]


@dataclass
class MandalReportOfDay:
	mandal_id: int
	mandal_name: str
	total_cases: int
	total_deaths: int
	total_recovered_cases: int

@dataclass
class DistrictReportOfDay:
	district_name: str
	mandals: List[MandalReportOfDay]
	total_cases: int
	total_deaths: int
	total_recovered_cases: int

@dataclass
class Statistics:
	date: datetime.date
	total_cases: int
	total_deaths: int
	total_recovered_cases: int

@dataclass
class MandalStatistics:
	mandal_id: int
	mandal_name: str
	reports: List[Statistics]

@dataclass
class DayWiseMandalDetailsDto:
	district_name:str
	mandals: List[MandalStatistics]
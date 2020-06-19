from covid_dashboard.interactors.storages.dtos import DistrictReportDto


class ExtractReport:

    def extract_report(self, report_dto: DistrictReportDto) -> tuple:

        total_confirmed = report_dto.total_confirmed
        total_deaths = report_dto.total_deaths
        total_recovered = report_dto.total_recovered
        return total_confirmed, total_recovered, total_deaths
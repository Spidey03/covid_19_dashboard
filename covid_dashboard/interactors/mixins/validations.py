import datetime
from covid_dashboard.exceptions.exceptions import *


class ValidationMixin:

    def get_state_details(self, state_id: int):

        state_dto = self.storage.get_state_details(
            state_id=state_id)
        return state_dto

    def validate_district_id(self, district_id: int):

        is_district_id_valid = self.storage.check_is_district_id_valid(
            district_id=district_id)
        is_district_id_not_valid = not is_district_id_valid
        if is_district_id_not_valid:
            raise InvalidDistrictId(district_id)

    def validate_date_format(self, date: datetime.date):

        format_str = '%d-%m-%Y'
        print(type(date))
        try:
            datetime_obj = datetime.datetime.strptime(date, format_str)
        except ValueError:
            raise InvalidDateFormat()
        date = datetime_obj.date()
        if type(date) != datetime.date:
            raise InvalidDateFormat()

    def validate_date(self, date: datetime.date):

        self.validate_date_format(date)
        today = datetime.date.today()
        if date > today:
            raise InvalidDate

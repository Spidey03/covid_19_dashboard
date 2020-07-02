from datetime import datetime

DEFAULT_DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_datetime(datetime_value):
    return datetime.strftime(
        datetime_value, "%Y-%m-%d %X")


    # return datetime.strftime(
    #     datetime_value, "%Y-%m-%d %X.%f")

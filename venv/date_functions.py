# Fonctions pour convertir les unités de temps

import datetime
from datetime import time


def get_dates(dates: list[tuple]) -> list[datetime.date]:
    list_of_dates: list[datetime.date] = list()
    try:
        for x in dates:
            formatted_date: datetime.date = x[0].date()
            list_of_dates.append(formatted_date)
    except TypeError as error:
        print("Type error while iterating on list of dates:" + error.__str__())
    return list_of_dates


def get_times(dates: list[tuple]) -> list[datetime.time]:
    list_of_times: list[time] = list()
    try:
        for x in dates:
            formatted_time: datetime.time = x[0].time()
            list_of_times.append(formatted_time)
    except TypeError as error:
        print("Type error while iterating on list of dates:" + error.__str__())
    return list_of_times

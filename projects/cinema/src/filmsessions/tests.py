from django.test import TestCase
import datetime
import pytz


class Session():
    def __init__(self, time_from, time_to):
        self.time_from = self.localize(time_from)
        self.time_to = self.localize(time_to)

    @classmethod
    def localize(cls, time):
        local = pytz.timezone('Europe/Kiev')
        return local.localize(time, is_dst=True)


def time_valid(time_from, time_to, s):
    print('test obj:', time_from.time(), time_to.time(), end='\n')
    print('check with:', s.time_from.time(), s.time_to.time(), end='\n')
    if (time_from < s.time_from and time_to < s.time_from) or (time_from > s.time_to and time_to > s.time_to):
        print(True)
        return True
    print(False)
    return False

local = pytz.timezone('Europe/Kiev')
time_from1 = datetime.datetime(2020, 2, 11, 12, 6)
time_to1 = datetime.datetime(2020, 2, 11, 13, 6)
s1 = Session(time_from=time_from1, time_to=time_to1)

time_from2 = datetime.datetime(2020, 2, 11, 14, 6)
time_to2 = datetime.datetime(2020, 2, 11, 16, 6)
s2 = Session(time_from=time_from2, time_to=time_to2)

sessions = [s1, s2]

time_from_new = local.localize(datetime.datetime(2020, 2, 11, 15, 36))
time_to_new = local.localize(datetime.datetime(2020, 2, 11, 16, 6))
all(time_valid(time_from=time_from_new, time_to=time_to_new, s=s) for s in sessions)

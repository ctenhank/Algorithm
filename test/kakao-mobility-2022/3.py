import datetime

class Duration:
    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second

    @property
    def in_days(self) -> int:
        return self.year * 365 + self.month * 12 + self.day

class DateTime:
    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second

    def __str__(self):
        return f'{self.year}'.rjust(4, '0') + ':' + \
        f'{self.month}'.rjust(2, '0') + ':' + \
        f'{self.day}'.rjust(2, '0') + ':' + \
        f'{self.hour}'.rjust(2, '0') + ':' + \
        f'{self.minute}'.rjust(2, '0') + ':' + \
        f'{self.second}'.rjust(2, '0')

    def __hash__(self):
        return self.year * (10 ** 4) + self.month * (10 ** 2) + self.day

    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __ne__(self, other):
        return hash(self) != hash(other)

    @classmethod
    def parse(cls, time: str):
        unit = time.split(':')

        year = int(unit[0])
        month = int(unit[1])
        day = int(unit[2])
        hour = int(unit[3])
        minute = int(unit[4])
        second = int(unit[5])

        return DateTime(year, month, day, hour, minute, second)

    @classmethod
    def parse_from_second_to_day(cls, time: str):
        unit = time.split(':')

        day = int(unit[0])
        hour = int(unit[1])
        minute = int(unit[2])
        second = int(unit[3])

        return DateTime(
            day=day,
            hour=hour, 
            minute=minute, 
            second=second
            )
    
    def add(self, time):
        second = self.second + time.second
        minute = self.minute + time.minute
        hour = self.hour + time.hour
        day = self.day + time.day
        month = self.month + time.month
        year = self.year + time.year

        if second > 59:
            second -= 60
            minute += 1
        
        if minute > 59:
            minute -= 60
            hour += 1
        
        if hour > 23:
            hour -= 24
            day += 1
        
        if day > 30:
            day -= 30
            month += 1
        
        if month > 12:
            month -= 12
            year += 1

        return DateTime(year, month, day, hour, minute, second)

    def difference(self, time):
        second = self.second - time.second
        minute = self.minute - time.minute
        hour = self.hour - time.hour
        day = self.day - time.day
        month = self.month - time.month
        year = self.year - time.year

        return Duration(year, month, day, hour, minute, second)


def get_save_period(days: list):
    first, last = days[0], days[-1]
    diff = last.difference(first)
    return diff.in_days + 1


def is_success(days: list):
    return get_save_period(days) == len(days)

def solution(s, times):
    day = DateTime.parse(s)
    save = set([])
    save.add(day)
    for time in times:
        day = day.add(DateTime.parse_from_second_to_day(time))
        save.add(day)
    save = sorted(list(save), key= lambda e: hash(e))
    return [
        1 if is_success(save) else 0,
        get_save_period(save)
    ]
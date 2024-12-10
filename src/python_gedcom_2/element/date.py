"""GEDCOM element consisting of tag `gedcom.tags.GEDCOM_TAG_DATE`"""

from datetime import datetime
from enum import Enum
from typing import List

from python_gedcom_2 import tags
from python_gedcom_2.element.element import Element
from python_gedcom_2.element.time import TimeElement


RETURN_FIRST_DATE = "first"
RETURN_SECOND_DATE = "second"

period_prefixes: List[str] = ["FROM", "TO"]

approximate_prefixes: List[str]  = ["ABT", "CAL", "EST"]

range_prefixes: List[str]  = ["BET", "AFT", "BEF"]


class DateType(Enum):
    UNKNOWN = 0,
    EXACT = 1,
    PERIOD = 2,
    RANGE = 3,
    APPROXIMATE = 4,

    @classmethod
    def from_date_value(cls, value: str):
        if value == "Y":
            return DateType.UNKNOWN
        if any([value.startswith(prefix) for prefix in period_prefixes]):
            return DateType.PERIOD
        if any([value.startswith(prefix) for prefix in range_prefixes]):
            return DateType.RANGE
        if any([value.startswith(prefix) for prefix in approximate_prefixes]):
            return DateType.APPROXIMATE
        return DateType.EXACT

class DateElement(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_type = DateType.from_date_value(self.get_value())

    def as_datetime(self) -> datetime:
        """Returns a datetime object representing the date and time of this element

        :rtype: A datetime object with the date and optionally time
        """
        if self.date_type == DateType.EXACT:
            date_len = len(self.get_value().strip().split(" "))
            if date_len == 3:
                d = self.__parse_full_date_string(self.get_value())
            elif date_len == 2:
                d = self.__parse_month_year_string(self.get_value())
            elif date_len == 1:
                d = self.__parse_year_string(self.get_value())
            else:
                raise Exception(f"Malformed Date Value: {date_len} {self.get_value()}")

            if self.has_time():
                d.combine(d.date(), self.__parse_time_string(self.get_time().get_value()).time())
            return d

        elif self.date_type == DateType.PERIOD:
            return None

        elif self.date_type == DateType.RANGE:
            return None

        elif self.date_type == DateType.APPROXIMATE:
            return None

        elif self.date_type == DateType.UNKNOWN:
            raise Exception("Tried to parse unknown date. Please check with is_unknown before trying to parse")


    def is_unknown(self) -> bool:
        return self.get_value().strip() == "Y"

    def has_time(self) -> bool:
        return self._is_tag_present(tags.GEDCOM_TAG_TIME)

    def get_time(self) -> TimeElement:
        return self.get_child_element_by_tag(tags.GEDCOM_TAG_TIME)

    @staticmethod
    def __parse_full_date_string(value: str) -> datetime:
        return datetime.strptime(value.strip(), "%d %b %Y")

    @staticmethod
    def __parse_month_year_string(value: str) -> datetime:
        return datetime.strptime(value.strip(), "%b %Y")

    @staticmethod
    def __parse_year_string(value: str) -> datetime:
        return datetime.strptime(value.strip(), "%Y")

    @staticmethod
    def __parse_time_string(value: str) -> datetime:
        return datetime.strptime(value, "%H:%M:%S.%f")
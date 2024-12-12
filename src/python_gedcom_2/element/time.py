from python_gedcom_2.element.element import Element
from datetime import datetime, time

class TimeElement(Element):
    def as_datetime(self) -> datetime:
        return datetime.strptime(self.get_value(), "%H:%M:%S.%f")

    def as_time(self) -> time:
        return self.as_datetime().time()
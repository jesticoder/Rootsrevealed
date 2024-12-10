from python_gedcom_2 import tags
from python_gedcom_2.element.date import DateElement
from python_gedcom_2.element.element import Element


class EventDetail(Element):
    """
    An EventDetail can be one of many kinds of actual Element. This is an abstract class to contain a lot of shared methods.
    (See page 29 of the GEDCOM 5.5 spec for details)
    NOTE: This is different from an event element, which is a legitimate GEDCOM tag and has its own rules.
    """

    def has_date(self) -> bool:
        """Returns True if this EventDetail has a DateElement as a child.
        """
        return self._is_tag_present(tags.GEDCOM_TAG_DATE)

    def get_date_element(self) -> DateElement | None:
        """Returns the DateElement of this EventDetail if it exists.
        """
        for child in self.get_child_elements():
            if isinstance(child, DateElement):
                return child

        return None

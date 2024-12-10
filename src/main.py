from klassen import *
from python_gedcom_2.parser import Parser

parser: Parser = Parser()

parser.parse_file(".\\gedcom_files\\The English and British Kings and Queens.ged")

elements: List[Element] = parser.get_root_child_elements()

for e in elements:
    
    if isinstance(e, IndividualElement):
        death = e.get_death_element()
        if not death or not death.has_date():
            continue
        print(death.get_date_element().as_datetime())

class Individual:                                                                                                       # Klasse aller einzelner Menschen
    def __init__(self, birth = None,death = None,info = {},last_name = "",first_name = "",child_in = None,parent_in = None): # birth und death haben datentyp event, child_in und parent_in haben datentyp Family
        self.birth = birth
        self.death = death
        self.info = info                                                                                               # Info soll alles rein was in diesen texten in gedcom steht 
        self.last_name = last_name
        self.first_name = first_name
        self.child_in = child_in
        self.parent_in = parent_in
        
    def get_children(self):                                                                                                 # gibt den Wert kinder von diesem Individuum zurück
        return self.parent_in.children

    def get_parents(self):                                                                                                  # selbes für Eltern
        return [self.child_in.mother,self.child_in.father]
    
    def get_generation(self):



class Family:                                                                                                           # stellt die Verbindung zwischen Individuen dar
    def __init__(self, mother = None,father = None,children = []):
        self.mother = mother
        self.father = father
        self.children = children


class Event:                                                                                                            # stellt Ereignisse wie den Tod und die Geburt eines Individuums dar
    def __init__(self, date = "",place = "",info = {}):
        self.place = place
        self.date = date
        self.info = info



# example family


# Ereignisse erstellen
birth_mother = Event(date="1980", place="Berlin")
birth_father = Event(date="1978", place="Hamburg")
birth_child = Event(date="2006", place="Hannover")

# Personen erstellen
mother = Individual(birth=birth_mother, first_name="Anna", last_name="Müller")
father = Individual(birth=birth_father, first_name="Peter", last_name="Müller")
child = Individual(birth=birth_child, first_name="Martin", last_name="Müller")

# Familie erstellen
family = Family(mother=mother, father=father, children=[child])

# Beziehungen setzen
mother.parent_in = family
father.parent_in = family
child.child_in = family

# Daten abrufen
print(f"Martins Eltern: {[parent.first_name for parent in child.get_parents()]}")
print(f"Anna's Kinder: {[kid.first_name for kid in mother.get_children()]}")



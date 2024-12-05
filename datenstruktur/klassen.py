class Individual:                                                                                                       # Klasse aller einzelner Menschen
    def __innit__(birth = None,death = None,info = {},last_name = "",first_name = "",child_in = None,parent_in = None): # birth und death haben datentyp event, child_in und parent_in haben datentyp Family
        self.birth = birth
        self.death = death
        self.info = info                                                                                               # Info soll alles rein was in diesen texten in gedcom steht 
        self.last_name = last_name
        self.first_name = first_name
        self.child_in = child_in
        self.parent_in = parent_in
        
    def get_children():                                                                                                 # gibt den Wert kinder von diesem Individuum zurück
        return self.parent_in.children

    def get_parents():                                                                                                  # selbes für Eltern
        return [self.child_in.mother,self.child_in.father]
    

class Family:                                                                                                           # stellt die Verbindung zwischen Individuen dar
    def __innit__(mother = None,father = None,children = []):
        self.mother = mother
        self.father = father
        self.children = children


class Event:                                                                                                            # stellt Ereignisse wie den Tod und die Geburt eines Individuums dar
    def __innit__(date = "",place = "",info = {}):
        self.place = place
        self.date = date
        self.info = info



# example family



martin = Individual(Event("2006","Hannover"))    #wie zum fick macht man ohne death und info




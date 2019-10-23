
#Beschreibung der Möbel. Stauraum besitzt Inhalt.


class furniture:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class storage(furniture):
    def __init__(self, name, location, content):
        furniture.__init__(self, name, location)
        self.content = content



#Beschreibung der interaktiven ("smarten") Geräte.
# Status = An/Aus; Operable = Fehlermeldung?


class interactiveAppliance:
    def __init__(self, status, operable):
        self.status = status
        self.operable = operable



#Beschreiung des vorhandenen Koch- und Essgeschirrs


class tools:
    def __init__(self, name, usage):
        self.name = name
        self.usage = usage


class container(tools):
    def __init__(self, name, usage, capacity):
        tools.__init__(self, name, usage)
        self.capacity = capacity


# groceries beschreibt alle Lebensmittel.
# name = Name; date_buy = Kaufsdatum; amount = Wie oft das selbe?; size = Größe der Portion
# category = Kategorie (Fleisch, Fisch, Gemüse, ...); allergen = Allergene

class groceries:
    def __init__(self, name, date_buy, amount, size, category, allergen):
        self.name = name
        self.date_buy = date_buy
        self.amount = amount
        self.size = size
        self.category = category
        self.allergen = allergen

class perishable(groceries):
    def __init__(self, name, date_buy, amount, size, category, allergen, expiry):
        groceries.__init__(self, name, date_buy, amount, size, category, allergen)
        self.expiry = expiry

class nonPerishable(groceries):
    def __init__(self, name, date_buy, amount, size, category, allergen):
        groceries.__init__(self, name, date_buy, amount, size, category, allergen)

class spice(groceries):
    def __init__(self, name, date_buy, amount, size, category, allergen):
        groceries.__init__(self, name, date_buy, amount, size, category, allergen)















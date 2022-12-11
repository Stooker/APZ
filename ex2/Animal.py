class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.type = "none"

    def get_name(self):
        print("To zwierze ma na imię: ", self.name)

    def get_age(self):
        print("Wiek: ", self.age)

    def get_type(self):
        print("Typ: ", self.type)

from Animal import Animal


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        self.type = "dog"

    def voice(self):
        print("Hau hau")

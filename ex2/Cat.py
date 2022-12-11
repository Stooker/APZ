from Animal import Animal


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        self.type = "cat"

    def voice(self):
        print("Miau")

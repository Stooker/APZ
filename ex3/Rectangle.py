class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if (a == b):
            self.type = "kwadrat"
        else:
            self.type = "prostokąt"

    def circuit(self):
        return 2 * self.a + 2 * self.b

    def field(self):
        return self.a * self.b

    def describe(self):
        if (self.type == "kwadrat"):
            print("Ta figura to ", self.type, " o boku:\n a = ", self.a)
        else:
            print("Ta figura to ", self.type, " o bokach:\n a = ", self.a, "\n b = ", self.b)

        print("Obwodzie:", self.circuit())
        print("I polu:", self.field())

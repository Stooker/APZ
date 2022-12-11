class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.type = "trójkąt"

    def circuit(self):
        return self.a + self.b + self.c

    def field(self):
        p = self.circuit() / 2
        field = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return field

    def describe(self):
        print("Ta figura to ", self.type, " o bokach:\n a = ", self.a, "\n b = ", self.b, "\n c = ", self.c)
        print("Obwodzie:", self.circuit())
        print("I polu:", self.field())

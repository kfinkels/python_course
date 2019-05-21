class CompressorBase:
    def __init__(self, path):
        self.path = path

    def compress(self):
        pass

    def something(cls, x):
        pass

    def __repr__(self):
        return f"path: {self.path}"


instance = CompressorBase("somepath")
print(repr(instance))


class Polynom:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return str([str(x) for x in self.coeffs])

    def __add__(self, other):
        self.coeffs += other.coeffs

p1 = Polynom([3, 5, 6]) # x3 + y5 + 6
p2 = Polynom(10, 11, 12)

print(p1+p2)

print(p1)
print(p2)

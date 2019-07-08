class Polynom:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

p1 = Polynom(2, 2, 3) # x^2 + 2x + 3
p2 = Polynom(3, 5, 3) # x^3 + 5x + 3

print(p1)
print(p2)

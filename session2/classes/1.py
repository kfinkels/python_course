class Polynom:
    pass

p1 = Polynom() # x^2 + 2x + 3
p2 = Polynom()

p1.coeffs = (2, 2, 3) # x^2 + 2x + 3
p2.coeffs = (3, 5, 3) # x^3 + 5x + 3

print(p1)
print(p2)

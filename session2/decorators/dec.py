from time import time


def add(x, y):
    return x + y


before = time()
print(add(10, 20))
after = time()
print(after - before)


before = time()
print(add(100, 100))
after = time()
print(after - before)


before = time()
print(add(-5, 15))
after = time()
print(after - before)

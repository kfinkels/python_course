from time import time


def timer(func):
    def f(x, y):
        before = time()
        value = func(x, y)
        after = time()
        print("elapsed", after - before)
        return value
    return f


def add(x, y):
    return x + y


add = timer(add)
print(add(10, 20))

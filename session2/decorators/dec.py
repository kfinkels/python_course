from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        value = func(*args, **kwargs)
        after = time()
        print("elapsed", after - before)
        return value
    return f


@timer
def add(x, y):
    return x + y


# add = timer(add)
print(add(10, 20))

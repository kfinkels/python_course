from time import time


def divide(x, y=1):
    return x / y


def logger(func):
    def wrapper(x, y=1):
        print(f"starting {func.__name__} at {time()}")
        value = func(x, y)
        print(f"finished {func.__name__} at {time()}")
        return value
    return wrapper


divide = logger(divide)
print(divide(10, 20))
print(divide(100, 100))
print(divide(-5, 15))


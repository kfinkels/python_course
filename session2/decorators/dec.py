from time import time


def logger(func):
    def wrapper(x, y=1):
        print(f"starting {func.__name__} at {time()}")
        value = func(x, y)
        print(f"finished {func.__name__} at {time()}")
        return value
    return wrapper


def saferun(func):
    def wrapper(x, y=1):
        try:
            func(x, y)
        except Exception as ex:
            print(f"Exception: {ex}")
    return wrapper

@saferun
@logger
def divide(x, y=1):
    return x / y


print(divide(10, 20))
print(divide(100, 100))
print(divide(-5, 15))
print(divide(-5, 0))


from inspect import getsource
from time import time


def log_func(og_func):
    print(f"log {og_func.__name__} at {time()}")


def logger(log_func):
    print("entered logger")

    def decorator(func):
        def wrapper(*args, **kwargs):
            log_func(func)
            value = func(*args, **kwargs)
            log_func(func)
            return value
        return wrapper
    return decorator


def saferun(func):
    print("entered saferun")
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f"Exception {ex}")
    return wrapper


@logger(lambda og_func: print(f"log {og_func.__name__} at {time()}"))
@saferun
def divide(x=2, y=1):
    return x / y

# divide.__name__
# divide.__module__
# divide.__defaults__
# divide.__code__.co_code
# divide.__code__.co_varnames
# print(getsource(divide))


params = [1, 2]
params_dict = {"x": 1, "y": 2}

# divide = saferun(logger(divide))
print(divide(**params_dict))
print(divide(10, 20))
print(divide(100, 100))
print(divide(-5, 15))
print(divide(-5, 0))


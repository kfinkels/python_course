from inspect import getsource
from time import time


def divide(x, y=1):
    return x / y


# divide.__name__
# divide.__module__
# divide.__defaults__
# divide.__code__.co_code
# divide.__code__.co_varnames
# getsource(divide())

print(f"starting {divide.__name__} at {time()}")
print(divide(10, 20))
print(f"finished {divide.__name__} at {time()}")


print(f"starting {divide.__name__} at {time()}")
print(divide(100, 100))
print(f"finished {divide.__name__} at {time()}")


print(f"starting {divide.__name__} at {time()}")
print(divide(-5, 15))
print(f"finished {divide.__name__} at {time()}")


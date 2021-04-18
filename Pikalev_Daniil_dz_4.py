from functools import wraps


def value_checker(check):
    def _valeu_checker(func):
        @wraps(func)
        def wrapper(*args):
            x = args[0]
            if check(x):
                return func(x)
            else:
                raise ValueError(f'wrong value {x}')
        return wrapper
    return _valeu_checker


@value_checker(lambda x: x>0)
def calc_cube(x):
    return x**3


print(calc_cube(5))
print(calc_cube(-5))

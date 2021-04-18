def args_type(func):
    def some_log(*args, **kwargs):
        for arg in args:
            print(f'{str(arg)}: {type(arg)}')
        for key, val in kwargs.items():
            print(f'{key} = {str(val)}: {type(val)}')
    return some_log


@args_type
def calc_cubes(*args, **kwargs):
    res_dict = []
    for number in args:
        res_dict.append(number**3)


print(calc_cubes(3, 5, abc='add'))

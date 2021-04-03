# def generate_nums(n):
#     for i in range(1, n+1, 2):
#         yield i
#
#
# generator = generate_nums(15)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

number = 15
my_numbers = (number for number in range(1, number+1, 2))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))

my_numbers = []

# создаем список из кубов чисел от 1 до 1000
for number in range(1, 1000, 2):
    cube = number ** 3
    my_numbers.append(cube)

new_numbers = []

# проходимся по каждому элементу списка и получаем сумму цифр каждого числа в списке
for i in my_numbers:
    result = 0
    test_element = i + 17
    while test_element != 0:
        result = result + test_element % 10
        test_element = test_element // 10

    bingo_number = 0

    # проверяем, подходит ли сумма цифр числа под наше условие, если подходит добавляем ее в новый список
    if result % 7 == 0:
        bingo_number = bingo_number + i
        new_numbers.append(bingo_number)

thesum = 0
# суммируем элементы в новом списке
for b in new_numbers:
    thesum = thesum + b
print(thesum)
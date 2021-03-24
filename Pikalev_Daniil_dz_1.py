numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}


def num_translate():
    word = input('Введите буквами число от одного до десяти на англйском языке: ')
    if word[0:1].islower():
        print(numbers.get(word))
    elif word[0:1].isupper():
        modify = word.lower()
        big_number = numbers.setdefault(modify)
        if big_number is None:
            print(None)
        else:
            print(big_number.capitalize())



num_translate()

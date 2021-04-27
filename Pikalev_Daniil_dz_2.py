class Zerobyzero(ZeroDivisionError):

    def __init__(self, txt):
        self.txt = txt

dividend = int(input('Введите делимое число: '))
devider = int(input('Введите делитель: '))

try:
    if devider == 0:
        raise Zerobyzero ('Деление на ноль недопустимо')
    else:
        quotient = dividend/devider
        print(f'Частное от деления равно: {quotient}')
except Zerobyzero as z:
    print(z.txt)



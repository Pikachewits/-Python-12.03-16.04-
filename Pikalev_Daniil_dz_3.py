class NumberError(ValueError):

    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    try:
        request = input('Введите число: ')
        if request == 'stop':
            break
        if not request.isdigit():
            raise NumberError('Это не число!')
        my_list.append(int(request))
    except NumberError as e:
        print(e.txt)
print(my_list)


peoples=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for name in peoples:
    new_peoples = name.split(' ')[::-1][0:1]
    print(f'Привет {new_peoples[0].capitalize()}!')
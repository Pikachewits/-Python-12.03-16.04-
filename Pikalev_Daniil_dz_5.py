prices = [57.8, 46.51, 97, 16.5, 69, 179.56, 1268, 2.6, 65.12, 88]

prices.sort()

count = 0
for i in prices:
    x = i
    a = int(x)
    b = (100 *(x-a))
    result = f'{a} руб. {round(b):02} коп.'
    prices.remove(i)
    prices.insert(count, result)
    count += 1

str_new_prices = ', '.join(prices)
print(str_new_prices)

rev_prices = str_new_prices.split(', ')
rev_prices.reverse()
print(rev_prices)

most_expensive = ', '.join(prices[-5:])

print(f'Цена 5-ти самых дорогих товаров: {most_expensive}')
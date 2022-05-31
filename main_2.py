prices, new_prices = [57.8, 46.51, 97.4, 86.5, 21.6, 98.2, 54.2, 45.6, 12.5, 86.5, 23.4], []

for price in prices:
    a = int(price)
    b = (price % int(price)) * 100
    b = int(round(b, 2))
    total_price = f'{a} руб. {b:02.0f} коп.'
    new_prices.append(total_price)
    total_price = None

print(new_prices)
print(f'id списка вначале : {id(new_prices)}')
new_prices.sort()
print(new_prices)
print(f'id списка после сортировки: {id(new_prices)}')

prices, new_prices = [57.8, 46.51, 97.4, 86.5, 21.6, 98.2, 54.2, 45.6, 12.5, 86.5, 23.4], []

for price in prices:
    a = int(price)
    b = (price % int(price)) * 100
    b = int(round(b, 2))
    total_price = f'{a} руб. {b:02.0f} коп.'
    new_prices.append(total_price)
    total_price = None

print(new_prices)
print(f'id списка вначале: {id(new_prices)}')
print(new_prices.sort(reverse=True))
print(f'id списка после обратной сортировки: {id(new_prices)}')
print(f'Пять самых дорогих товаров: {new_prices[:5]}')
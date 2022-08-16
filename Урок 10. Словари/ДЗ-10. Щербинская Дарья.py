#У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
#Выведите через ‘’–’’ название – цену – количество.
#С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.
product = {'каштан': [2.10, 10],  # Название - цена - кол-во
           'Столичное': [2.05, 10],
           'Топ': [1.54, 10],
           'Вавёрочка': [1.65, 10]}
total_price = 0  # Цена после первого выбора
full_price = 0   # Итоговая цена
print('Есть в наличии следующие варианты: ')
print('Варианты выводятся: "Название" - "Цена" - "Количество"')
for key, value in product.items():  # Цикл по ключам и значениям
    print(key, '-' , value[0], '-' , value[1])
count = 0
while True:
    name = input('Введите название мороженого: ')
    name = name.capitalize()
    if name == 'N':
        break
    elif name not in product.keys():
        print('Нет такого.')
        continue
    count = int(input('Введите количество мороженого: '))
    if name in product.keys():
        if count > product[name][1]:
            print('Такого количества нет.')
            continue
    product[name][1] -= count   # Оставшееся кол-во
    total_price = count * product[name][0]    # Цена за выбранное в первый раз
    full_price += total_price  # Финальная цена за все
    print('С вас за все', round(full_price, 2), 'бел. руб.')
    print('------------------------------------')
    for key, value in product.items():
        print(key, '-', value[0], '-', value[1])


a = input("Введите первую строку")
b = input("Введите вторую строку")
c = input("Введите символ")
d = ''
for i in a:
    if i != b:
        d += i  # тоже самое что с = с+i

print('Результат:', d)
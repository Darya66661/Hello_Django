#Определить, является ли год високосным

years = int(input("Введите год"))

if years/400 == 0:
    print("Высокосный")
elif years/100 == 0:
    print("Не высокосный")
elif years/4 == 0:
    print("Высокосный")
else:
    print("Не высокосный")
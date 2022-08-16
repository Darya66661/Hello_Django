#1.	Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
#Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
#После этого удалите созданную папку.
#Все операции выполнять с помощью встроенных функций библиотеки os.

# import os
# os.mkdir('Новая папка')
# os.chdir('Новая папка')
# a1 = open('test_1.txt','w')
# a2 = open('test_2.txt','w')
# a3 = open('test_3.txt','w')
# a1.close()
# a2.close()
# a3.close()
# os.rename('test_1.txt','rename_1.txt')
# os.rename('test_2.txt','rename_2.txt')
# os.rename('test_3.txt','rename_3.txt')
# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
# os.chdir("..")
# os.rmdir('Новая папка')

#2.	Даны два кортежа: C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
#C_2 = (45, 21,124,76,5,23,91,234)
#Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей.

# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# a = 'C_1' if sum(C_1) > sum(C_2) else 'C_2'
# print(f'Сумма больше в кортеже -  {a}')
# print('max номер', max(C_1), 'порядкового элемента:', C_1.index(min(C_1)))
# print('min номер', min(C_2), 'порядкового элемента:', C_2.index(min(C_2)))


#3.	Напишите программу, демонстрирующую работу try\except\finally.

# try:
#    a = input("Введите первое число:")
#    b = input("Введите второе число:")
#    print("Результат: ", int(a) / int(b))
# except(ValueError, ZeroDivisionError):
#    print("Ошибка!")
# finally:
#    print("Конец программы!")

#4.	Создайте 2 множества:
#- Если они одинаковые: вывести что они равны
#- Если 1 множество полностью состоит из второго: вывести сообщение множество 1 состоит из множества2
#- Если 2 множество полностью состоит из 1: вывести сообщение множество 2 состоит из множества 1
#- Если они пересекаются: вывести элементы в которых они пересекаются
#- Если не пересекаются: вывести сообщение об этом

# import random
# a = set([random.randint(0, 100) for i in range(9)])
# b = set([random.randint(0, 100) for i in range(4)])
# print(a)
# print(b)
# if a == b:
#     print('Множества равны!')
# else:
#     print('Множества не равны!')
# if a - b == set():
#     print('Множество 1 состоит из множества 2')
# if b - a == set():
#     print('Множество 2 состоит из множества 1')
# if a.intersection(b):
#     print('Пересечение:', a & b)
# else:
#     print("Пересечений нету")

#5.	Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

# a = 'An apple a day keeps the doctor away'
# b = {i: a.count(i) for i in a}
# print(b)

#6.	Ввести 10 чисел, данные числа добавить их во множество.

# i = 0
# b = set()
# while i < 10:
#     i = i + 1
#     a = input('Введите число: ')
#     b.add(a)
# print(b)

#7.	Найти самое длинное слово в строке.
# a = "Стаффордширский терьер ретив, а черношерстный ризеншнауцер резв"
# print(max(a.split(), key = len))

#8.	Есть словарь песен группы Depeche Mode violator songsdict =
# { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут.
#Создайте новый словарь тех песен, в название которых состоит из одного слова

# songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
#              'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68,}
# a = songsdict.values()
# b = songsdict.keys()
# c = 0
# d = []
# e = []
# for i in a:
#     c = c + i
# print('Общее время звучания всех песен', c)
# for i in songsdict:
#     if songsdict[i] > 5:
#             d.append(i)
#             print('Cписок песен, время звучаниях которых больше 5 минут' , d)
# for i in b:
#     if ' ' in i:
#         continue
#     e.append(i)
# print("Cловарь тех песен, в название которых состоит из одного слова", e)

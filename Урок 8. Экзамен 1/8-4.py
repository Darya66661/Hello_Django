# 4. Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно.
m = int(input("Введите первое целое число: "))
n = int(input("Введите второе целое число: "))
if m<=n:
    for i in range(m, n+1):
        print(i, end=" ")

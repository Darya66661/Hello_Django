#перемножить все четные цифры от 0 до 125, результат вывезти на экран
i = 1
res = 1
while i <= 125:
        if i % 2 == 0:
           res = res * i
        i += 1
print(res)
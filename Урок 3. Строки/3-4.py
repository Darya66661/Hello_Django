#Вычислить сумму цифр случайного трехзначного числа с помощью среза

import random
a = random.randint(100,999)
print(a)
y = str(a)
b = int(y[0])
c = int(y[1])
d = int(y[2])
print(b+c+d)

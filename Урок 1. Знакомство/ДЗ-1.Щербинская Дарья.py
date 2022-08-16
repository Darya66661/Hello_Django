#Вычислить сумму цифр случайного трёхзначного числа


import random
a = random.randint(100,999)
print(a)
print("сумма:", a//100+a//10%10+a%10)













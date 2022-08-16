import random
import random
a = [random.randint(0, 5) for i in range(10)]         #рандомный список
b = tuple(a)           #преобразовать кортеж
c = [random.randint(-5, 0) for i in range(10)]         #рандомный список
d = tuple(c)           #преобразовать кортеж

y = b + d
print("количество нулей", y.count(0))


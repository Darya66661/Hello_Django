import random
a = [random.randint(0, 10) for i in range(10)]         #рандомный список
b = tuple(a)           #преобразовать кортеж
print(b)
print('max', max(b), 'min', min(b))


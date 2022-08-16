a = {1,2,3,4,5,(3,9)}       #множества с кортежем
print(a)

b = {'Darya', 'Valeriya', 'Evgeniy', 'Polina'}            # множества поддерживают разные типы данных
print(b)

c = set([1,2,3,4,5])          #метод создания множеств, изменяемый тип данных
print(c)

d = {1,2,3,4,5,1,2,3,4}           #множество уникально и выводит без дубликата
print(d)

e = {}                      #создает словарь
print(type(e))            #определяет тип

x = set()                   #создаем множество
print(type(x))

months = set(['jan', 'feb', 'march', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])    #через цикл можно пройти все элементы множестваs
#for months

print('may' in months)           #наличие элемента в множестве
months.add('fed')      #добавление элемента в любое место

d = {1,2,3,4,5,1,2,3,4}
d.discard(3)         #не будет выдавать ошибку если нет элемента
#d.remuve(8)              #будут выдавать ошибку
print(d)

d = {1,2,3,4,5}
d.pop()             #удаление произвольного элемента если пустой
print(d)
d.clear()              #удаляет все элементы во множестве
print(d)

months = set(['jan', 'feb', 'march', 'apr', 'may', 'jun'])       #замена фигур скобкам set только с ними
months_1 = set(['jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
all_months = months.union(months_1)                                               #обьединение множеств

x={1,2,3}
y={4,3,6}
z={7,4,9}
c = x.union(y,z)         #обьединяет и игнорирует дубликаты
print(c)
print(x|y|z)          #обьединяет и разделяет множества(оператор-палочка)

x={1,2,3}
y={4,3,6}
print(x & y)              # пересечение множест, оператор & ищет элемент которые есть и в первом и втором

A={1,2,3}
B={4,3,6}
print(A-B)               #нахождение разницы между множествами
print(B-A)

b = {'Darya', 'Valeriya', 'Evgeniy', 'Polina'}            #возвращает копию множества
x = b.copy()
print(x)


b = {'Darya', 'Valeriya', 'Evgeniy', 'Polina'}
c = {'Darya', 'Valeriya', 'Evgeniy', 'Elena'}
x = b.isdisjoint(c)       #провкряет есть ли общие элемента, если есть выводит Folse, если нет True
print(x)

b = {'Darya', 'Valeriya', 'Evgeniy', 'Polina'}
print(len(b))            # возвращает длинну множества

n = frozenset([1,2,3,4,5])
print(type(n))        # неизменяемый тип данных

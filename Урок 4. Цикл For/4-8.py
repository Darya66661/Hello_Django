a = [10, 2, 3]
print(a)
a.append(7)      #добовление элемента в конец списка
print(a)

a = [10, 2, 2, 8, 2]
print(a)
b = a.count(2)   #считает сколько элементов в списке в скобках
print(b)


a = [10, 2, 2, 8, 2]
print(a)
b = a.index(2)   #узнать индекс заданного элемента, индексация с 0 наченаеться
print(b)

a = [10, 2, 2, 8, 2]
b = a.pop(2)   #удаляет индекс элемента из списка, и выводит какой элемент удалил, выводит список с удаленным списком,
print(b)
print(a)

a = [10, 2, 2, 8, 2]
print(a)
b = a.remove(2)   #удаляет сам элемент, только первый найденный
print(a)


a = [10, 2, 2, 8, 2]
print(a)
b = a.reverse()   #переворачивает список
print(a)


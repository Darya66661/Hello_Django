elements = []
elements.append('a')   #добавление в конец списка
elements.append(1)
print(elements)

elements = [1,3,'a',6,'b']
elements.insert(1,2)   #добовление на указанную позицию
print(elements)


elements = [1,3,'a',6, 'b']
elements[1] = 2    #изменение элемента в списке (замена элемента)
print(elements)

elements = [1,3,'a',6, 'b']
elements[1] = 2    #удаление элемента в списке
print(elements)

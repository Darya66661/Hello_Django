# 11. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы, которые содержат пробел.
a = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
b = []
for i in a:
    if ' ' in i:
        b.append(i)
print(b)
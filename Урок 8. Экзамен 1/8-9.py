# 9. Дан список [student1, student2, student3] с помощью цикла for добавить к каждому элементу списка слово “_good”. Вывести на экран.
a = ['student1','student2','student3']
b = []
c = '_good'
for i in a:
    i = i + c
    b.append(i)
print(b)

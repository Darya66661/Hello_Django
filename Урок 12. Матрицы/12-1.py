# a =[[1,4,5,],
#    [5,8,9]]
# print(a)

a = 3              # строки
b = 2               #   столбики
c = []
for i in range(a):
    c.append([0]*b)
print(c)

a = 3              # строки
b = 2               #   столбики
c = [[0] * b for i in range(a)]
print(c)

a = [[1,4,5,12],
     [-5,8,9,0],
     [-6,7,11,19]]
print('a=', a)
print('a[1]=',a[1]) #вторая строка
print('a[1][2]=', a[1][2])  # третий элемент второй строки
print('a[0][-1]=', a[0][-1]) #последний элементпервой строки
column = [];    #пустой список
for row in a:
    column.append(row[2])
    print('3rd column =', column)

a = [[1,2,3,4], [5,6], [7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

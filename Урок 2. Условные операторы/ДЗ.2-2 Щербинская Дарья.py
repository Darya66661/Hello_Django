#Определить существование треугольника и его тип

#существование треугольника:
print("Введите стороны треугольника: ")
a = float(input("Сторона А = "))
b = float(input("Сторона B = "))
c = float(input("Сторона C = "))
if a+b>c or a+c>b or b+c>a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
#тип:
if a>b>c or a>c>b or b>a>c or b>c>a :
    print("Разносторонний треугольник")          #все стороны имеют разную длину
elif a==b or c==a or b==c:
    print("Равнобедренный треугольник")          #любые 2 стороны равны
elif a==b==c:
    print("Равносторонний треугольник")          #все стороны равны

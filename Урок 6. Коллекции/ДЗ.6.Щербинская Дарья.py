#Дан список list=[15,48,'hello',6,19,'world’].
#Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
#Все слова: посчитать количество гласных и согласных.
#Вывести всё на экран.


list = [15, 48, 6, 19, 'world','hello']
glass = 0
sogl = 0
print(list)
for i in list:
    if type(i) == int:
        if i%2 ==0:
            a = i//10 + i%10
            print('сумма цифр четного числа',i,'=', a)
        else:
            index = list.index(i)
            list[index] = 1
    else:
        for g in i:
            if g in 'aeyuio':
                glass = glass + 1
            else:
                sogl = sogl + 1
print(list,'Все согласные заменены на 1')
print(glass,'Гласных букв в списке')
print(sogl,'Согласных букв в списке')
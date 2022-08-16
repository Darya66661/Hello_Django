#1.	Реализовать калькулятор с 4 методами: Сумма, вычитаниеб , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат. Невалидные данные должны быть обработаны
# class Calculator:
#     def valdate_numbers(selfself, first_number, second_namder):
#         is_valid_first_namber = isinstance(first_number, int) or isinstance(first_number, float)
#         is_valid_second_namber = isinstance(second_namder, int) or isinstance(second_namder, float)
#         if is_valid_first_namber and is_valid_second_namber:
#             print('Valid')
#         else:
#             raise Exception('No Valid')
#     def summ(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         sum = first_number + second_number
#         return sum
#     def difference(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         diff = first_number - second_number
#         return diff
#     def multiplication(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         multip = first_number * second_number
#         return multip
#     def devision(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         if second_number == 0:
#             print('На 0 делить нельзя!')
#         else:
#             div = first_number / second_number
#             print(div)
#         return
# my_calc = Calculator()
# print(my_calc.summ(1,2))
# print(my_calc.difference(1,2))
# print(my_calc.multiplication(1,2))
# print(my_calc.devision(1,0))

#2.	Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента. Класс студен описан следующим образом:
# class Student:
#     def __init__(self, name, money):
#         self.name = name
#         self.name = money
#Необходимо понять у кого больше всего денег и вернуть его имя. Если у студентов денег поровну вернуть: “all”.
class Student:
    def __init__(self, name, money):
        self.name = name
        self.name = money
student_1 = Student("Petya", 100)
student_2 = Student("Kolya", 110)
student_3 = Student("Nikolay", 1000)
students = [student_1, student_2, student_3]
moneys = []
for student in students:
    moneys.append(student.money)
print(moneys)
if max(moneys) == min(moneys):
    print('all')
else:
    max_money = 0
for student in students:
    if student.money > max_money:
            name = student.name
print(max_money)
print(name)

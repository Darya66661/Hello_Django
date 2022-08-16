# class Human: #создание клаасса
#   #  pass
# my_human=Human   #экземпляр класса+имя класса
# print(dir(Human))        #список отрибутов класса

# class Human:
#     def __init__(self, name, age):            #динамическое поле, на уровне экземпляра класса
#         self.name = name     #Глобальные переменныее
#         self.age = age
#     def walk(self, km):
#         if km > 5:
#             return f'Я не могу пройти {km} км'
#         else:
#             return f'Я могу пройти {km} км'
# my_human = Human('Darya', 31)
# km = int(input('Введите км '))
# print((my_human.walk(km)))
# print(my_human.name)
# print(dir(my_human))
# print(my_human.age)

#Статические поля(переменные) которые обьявляються внутри тела класса
class Car:
    default_color = 'Grey'
    default_weight = 5000
def __init__(self, color, model):
    #Динамические поля
    self.color = color
    self.model = model
    def turn_on(self):
        pass


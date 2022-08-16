# class Human:
#     #Статические поля
#     default_name = "No name"
#     default_age = 0
#     def __init__(self, name=default_name, age=default_age):
#     #Динамические поля
#     #Публичные
#         self.name = name
#         self.age = age
#     #Приватные
#         self.__money = 0
#         self.__house = None
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
#     @staticmethod
#     def default_info():
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Age: {Human.default_age}')
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')
#
# Human.default_info()
# alexander = Human('Sasha, 27')
# alexander.info()
# alexander.earn_money(5000)
# alexander.earn_money(20000)
# alexander.info()

#родительский класс
class Phone:
    #Иницилизатор
    def __init__(self):
        self.is_on = False
    #Включаем телефон
    def turn_on(self):
        self.is_on = True
    #Есди телефон включен делаем звонок
    def call(self):
        if self.is_on:
            print('Making call...')
    #Унаследованный класс
class MobilePnone(Phone):
    #Добавляем новое свойство battery
    def __init__(self):
        super().__init__()
        self.battery = 0
    #Заряжаем телефон на величину переданного значения
def charge(self, num):
    self.battery = num
    print(f'Charging battery up to ... {self.battery}%')
my_mobile_phone = MobilePnone()
print(dir(my_mobile_phone))
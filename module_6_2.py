class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Доступные цвета

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner  # владелец транспорта. (владелец может меняться)
        self.__model = __model  # модель (марка) транспорта. (мы не можем менять)
        self.__engine_power = __engine_power  # мощность двигателя. (мы не можем менять)
        self.__color = __color  # название цвета. (мы не можем менять)

    def get_model(self):  # Вернуть модель транспорта
        return f'Модель: <{self.__model}>'

    def get_horsepower(self):  # Вернуть мощность двигателя
        return f'Мощность двигателя: <{self.__engine_power}>'

    def get_color(self):
        return f'Цвет: <{self.__color}>'  # Вернуть цвет транспорта

    def print_info(self):  # Информация о ТС включая имя водителя
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: <{self.owner}>')

    def set_color(self, new_color: str):  # Проверяем возможность изменения цвета
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на <{new_color}>')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Код проверки
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
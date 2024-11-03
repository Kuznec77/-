def type_int(value, num):  # Функция для проверки типа данных
    def break_code(numb):
        return num if isinstance(numb, int) else False
    if not break_code(num):
        print(f"{num} => {type(num)} {value}")

class House:
    houses_history = []

    def __new__(cls, name, *args, **kwargs):
        house = super().__new__(cls)
        house.name = name
        cls.houses_history.append(house.name)
        return house

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return type_int(self, self.number_of_floors) < type_int(self, other)

    def __le__(self, other):
        return type_int(self, self.number_of_floors) <= type_int(self, other)

    def __gt__(self, other):
        return type_int(self, self.number_of_floors) > type_int(self, other)

    def __ge__(self, other):
        return type_int(self, self.number_of_floors) >= type_int(self, other)

    def __ne__(self, other):
        return type_int(self, self.number_of_floors) != type_int(self, other)

    def __add__(self, value):
        return type_int(self, self.number_of_floors) + type_int(self, value)

    def __iadd__(self, value):
        return self.__add__(type_int(self, value))

    def __radd__(self, value):
        return self.__add__(type_int(self, value))

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
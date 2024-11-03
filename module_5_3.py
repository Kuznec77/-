def type_int(value, num):  # Функция для проверки типа данных
    if isinstance(num, int):
        return num
    else:
        print(f"{num}, {value}")

class House:
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



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
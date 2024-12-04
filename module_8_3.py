class IncorrectVinnumber(Exception):
    def __init__(self, message) -> None:
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message) -> None:
        self.message = message

class Car():
    def __init__(self, model, vin, numbers) -> None:
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        Car.__is_valid_numbers(numbers)
        Car.__is_valid_vin(vin)

    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinnumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinnumber('Неверный диапазон для vin номера')
        return True
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinnumber('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectVinnumber('Неверная длина номера, нет 6 символов')
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinnumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinnumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinnumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
def personal_sum(numbers):
    result = 0          # сумма чисел в коллекции numbers
    incorrect_data = 0  # кол-во некорректных данных
    for number in numbers:
        try:
            result += number
        except TypeError:   # несоответствие типов данных
            incorrect_data += 1
            print(f'Присутствует некорректный тип данных для подсчёта суммы - "{number}" - {type(number).__name__}')
    return (result, incorrect_data)

def calculate_average(numbers):
    res = 0
    try:                    # Проверяем, что numbers - это коллекция
        c = len(numbers)    #  Коллекция позволяет определить размер
        try:
            d = personal_sum(numbers)   # функция возвращает кортеж из двух значений
            res = d[0]/(c - d[1])
        except ZeroDivisionError:
            res = 0
    except TypeError:  # Передана не коллекция
        print(f'В numbers записан некорректный тип данных (не является коллекцией)')
        res = None
    return res

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать







def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Присутствует некорректный тип данных для подсчёта суммы - "{number}" - {type(number).__name__}')
    return (result, incorrect_data)

def calculate_average(numbers):
    res = 0
    try:
        c = len(numbers)
        try:
            d = personal_sum(numbers)
            res = d[0]/(c - d[1])
        except ZeroDivisionError:
            res = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных (не является коллекцией)')
        res = None
    return res

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

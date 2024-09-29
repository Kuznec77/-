my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
print('Список', my_list, 'Положительные числа из списка')
while count < len(my_list):
    num = my_list[count]
    count = count + 1
    if num == 0:
        continue
    elif num < 0:
        print('Встретилось отрицательное число:', num)
        break
    elif count == len(my_list):
        print(num)
        print('Список закончился')
    else:
        print(num)
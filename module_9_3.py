first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if not len(s1) == len(s2))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Jonny','Bilbo','Steve','Khendrik','Aaron'}
averagescores = {}  # создадим пустой словарь (средних баллов)
# Упорядочим имена учеников из Множества students для создания ключей словаря
names = list(students)  # преобразуем множество
names.sort()            # в упорядоченный список
# Заполним словарь средними баллами учеников
averagescores.update({names[0]:sum(grades[0])/len(grades[0]), names[1]:sum(grades[1])/len(grades[1])})
averagescores.update({names[2]:sum(grades[2])/len(grades[2]), names[3]:sum(grades[3])/len(grades[3])})
averagescores.update({names[4]:sum(grades[4])/len(grades[4])})
print('Средние баллы учеников -', averagescores)
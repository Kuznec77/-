team1_num = 5
team2_num = 6

print('В команде Мастера кода участников: %s !' % team1_num)


print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2

print('Команда Волшебники данных решила задач: {} !'.format(score_2))

team1_time = 18015.2
team2_time = 2153.31451
time_avg = (team2_time + team1_time) / tasks_total

print(' Волшебники данных решили задачи за {} с !'.format(team1_time))

print(f'Команды решили {score_1} и {score_2} задачи.')


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result

print(f'Результат битвы: {challenge_result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

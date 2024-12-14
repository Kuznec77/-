
from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for num in range(word_count):
            file.write(f'Какое то слово № {num+1}''|n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_result = time_end - time_start
print(f'Работа потоков {time_result}')

time_start = datetime.now()

thr_first = Thread(target = write_words, args = (10,'example5.txt'))
thr_second = Thread(target = write_words, args = (30,'example6.txt'))
thr_thrid = Thread(target = write_words, args = (200,'example7.txt'))
thr_fourth = Thread(target = write_words, args = (100,'example8.txt'))

thr_first.start()
thr_second.start()
thr_thrid.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_thrid.join()
thr_fourth.join()

time_end = datetime.now()
time_result = time_end - time_start
print(f'Работа потоков {time_result}')
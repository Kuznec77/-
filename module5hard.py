import time


class User:
    '''
    Класс для преобразования данных о пользователе
    '''

    def __init__(self, nickname, password, age):
        self.nickname = nickname  # Имя пользователя
        self.password = hash(password)  # Хеш пароль
        self.age = age  # Возраст

    def __str__(self):  # Необходимо для отображения в консоли
        return f"{self.nickname} ({self.age})"


class Video:
    '''
    Класс для преобразования данных о видео.
    '''

    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # Заголовок видео
        self.duration = duration  # Длительность видео
        self.adult_mode = adult_mode  # 18+
    def __str__(self):
        return self.title

class UrTube:
    """

    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True

    def register(self, nickname, password, age):
        if self.log_in(nickname, password):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))  # Регистрация пользователя
            self.current_user = self.users[-1]
            print(f"Пользователь {str(self.users[-1])} успешно зарегистрирован")

    def log_out(self):
        self.surrent_user = None

    def add(self, *videos):
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(str(video))
        return result

    def watch_video(self, video_title):  # Просмотр видео
        if self.current_user is None:  # Проверяем авторизацию
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18 and any(
                [video.adult_mode for video in self.videos if video.title == video_title]):  # 18+
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for video in self.videos:  # Запуск найденного видео
                if video.title == video_title:
                    print("Просмотр видео", video_title)
                    print("Время просмотра:", end="")
                    for sec in range(video.duration):
                        print(sec, end=" ")
                        time.sleep(1)
                    print("Конец видео")
                    break

# Код программы
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

from time import sleep
from random import randint

class UrTube:
    def __init__(self):
        self.users = []                  # users(список объектов User)
        self.videos = []                 # videos(список объектов Video)
        self.current_user = None         # current_user(текущий пользователь)

    def log_in(self, login, password): # поиск пользователя в users
        temp = 0
        for i in self.users:
            if i.nickname == login:
                if i.password == hash(password):
                    self.current_user = i
                else:
                    print('Неверный пароль')
            else:
                temp += 1
        if temp == len(self.users):
            print('Пользователь не найден')



    def register(self, nickname, password, age):
        if not (self.users):
            self.users.append(User(nickname, hash(password), age))
            self.current_user = User(nickname, hash(password), age)
        else:
            _len = len(self.users)
            count = 0
            for i in range(_len):
                if self.users[i].nickname == nickname:
                    count += 1
            if count == 0:
                self.users.append(User(nickname, hash(password), age))
                self.current_user = User(nickname, hash(password), age)
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if not(self.videos):
                self.videos.append(arg)
            else:
                _len = len(self.videos)
                count = 0
                for i in range(_len):
                    if self.videos[i] == arg:
                        count += 1
                if count == 0:
                    self.videos.append(arg)


    def get_videos(self, code_word):
        _list = []
        for i in self.videos:
            if i.title.lower().find(code_word.lower()) != -1:
                _list.append(i.title)
        return _list

    def watch_video(self, name_video):
        for i in self.videos:
            if i.title == name_video:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    while i.time_now < randint(3,10):
                        i.time_now += 1
                        sleep(1)
                        print(i.time_now, end=' ')
                    print('Конец видео')
                    i.time_now = 0



class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title               # title(заголовок, строка)
        self.duration = duration         # duration(продолжительность, секунды)
        self.time_now = time_now         # time_now(секунда остановки(изначально 0))
        self.adult_mode = adult_mode     # adult_mode(ограничение по возрасту, bool(False по умолчанию))

    def __eq__(self, other):
        return self.title == other.title

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # nickname(имя пользователя, строка)
        self.password = password  # password(в хэшированном виде, число)
        self.age = age            # age(возраст, число)

    def __str__(self):
        return self.nickname

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
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

from random import randint

class Person:
    user_name = 'Wickedsick'
    email = 'wickedsick225@yandex.ru'
    password = 'Ewq12345'

class RandomData:
    user_name = 'Тестик'
    email = f'test{randint(0,999)}@yandex.ru'
    password = f'{randint(1000,9999)}ewq'
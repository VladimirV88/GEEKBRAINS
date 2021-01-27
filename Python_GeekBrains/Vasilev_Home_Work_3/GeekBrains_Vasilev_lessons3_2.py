"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def users_param(name, lastname, birthday, city, email, mobile_phone):
    return name, lastname, birthday, city, email, mobile_phone


print(users_param(name='Vladimir', lastname='Vasilev', birthday='13.01.1988', city='Saint-Petersburg', email='none',
                  mobile_phone='8901234567'))

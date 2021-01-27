"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
first = int(input('Введите первое число  '))
second = int(input('Введите второе число  '))
third = int(input('Введите третье число  '))
# first, second, third = int(input("Введите первое число")), int(input('Введите второе число  ')), int(input('Введите третье число  '))

def my_func(a, b, c):
    """
    находим минимальное число и отнимаем его от суммы
    :param b: second
    :param a: first
    :param c: third
    """
    min_value = min(a, b, c)
    return a + b + c - min_value


print(my_func(first, second, third))

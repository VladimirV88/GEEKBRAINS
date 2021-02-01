"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    pass


def numb_input():
    return int(input("Введите числитель: "))


def numb_input2():
    numb_b = int(input("Введите знаменатель: "))

    if numb_b == 0:
        raise MyZeroDivisionError
    return numb_b


while True:
    try:
        numb = numb_input()
        numb2 = numb_input2()

        print(f"Результат деления равен:  {numb / numb2}")
    except MyZeroDivisionError:
        print("Деление на ноль запрещено!")


"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
result_a = int(input(f"Введите числитель 'a' "))
result_b = int(input(f"Введите делитель 'b' "))


def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка, деление на ноль запрещено")


total_result = my_func(result_a, result_b)
print(total_result)
# print(my_func(result_a, result_b))

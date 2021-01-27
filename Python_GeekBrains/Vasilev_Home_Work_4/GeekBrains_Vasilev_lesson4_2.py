"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
#from random import randrange, shuffle, randint, random

user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#user_list = [randrange(1, 100) for _ in range(10)]
print('Исходный список: ', user_list)

result_list = [
    val for idx, val in enumerate(user_list)
    if idx > 0 and user_list[idx - 1] < val
]
print('result: ', result_list)

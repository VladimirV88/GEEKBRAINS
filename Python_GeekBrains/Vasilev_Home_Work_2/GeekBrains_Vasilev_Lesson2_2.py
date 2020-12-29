"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []
max_list = int(input('Укажите длину списка '))

while len(my_list) < max_list:
    my_last = int(input(f'Введите числа, ввод ограничен указанной максимальной длиной списка {max_list} '))
    my_list.append(my_last)

print(f'Полученный список {my_list}')
my_last = None
for i in range(0, (len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1)):
    if i % 2 != 0:
        my_list[i] = my_last
    else:
        my_last = my_list[i]
        my_list[i] = my_list[i + 1]
print('Реализуем обмен значений соседних элементов', my_list)

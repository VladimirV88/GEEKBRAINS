"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
my_file = "lesson5.txt"

with open(my_file, "w") as create_file:
    numb = input("Введите набор чисел, разделенных пробелами: ")
    create_file.write(numb)

with open(my_file, "r") as source_file:
    first_string = source_file.readline()
    nums = first_string.split(" ")
    summa = 0
    for el in nums:
        summa += int(el)

print(f"Сумма чисел равна {summa}")

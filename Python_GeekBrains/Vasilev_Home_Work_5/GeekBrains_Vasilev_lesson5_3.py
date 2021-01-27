"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
source = "lesson3.txt"

with open(source, "r") as source_file:
    content = source_file.read()

content_list = content.split("\n")
str_count = len(content_list)
total_salary = 0

print("Сотрудники у кого оклад меньше 20000:")
for el in content_list:
    el_str = el.split(" ")
    total_salary += float(el_str[1])
    if float(el_str[1]) < 20000:
        print(f"{el_str[0]} оклад = {el_str[1]}")

print(f"Средний доход сотрудников равен {round(total_salary / str_count)}")

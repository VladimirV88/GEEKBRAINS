"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

source = "lesson2.txt"

with open(source, "r") as source_file:
    content = source_file.read()

content_list = content.split("\n")
str_count = len(content_list)

print(f"Количество строк в файле {source}: {str_count}")
print("Количество слов по строкам:")

i = 1
for el in content_list:
    el_str = el.split(" ")
    print(f"строка № {i}: {len(el_str)}")
    i += 1

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
source = open("lesson4.txt", "r")
target = open("lesson4_out.txt", "w")

for content in source:
    if content.find('One') >= 0:
        content = content.replace('One', 'Один')
    if content.find('Two') >= 0:
        content = content.replace('Two', 'Два')
    if content.find('Three') >= 0:
        content = content.replace('Three', 'Три')
    if content.find('Four') >= 0:
        content = content.replace('Four', 'Четыре')
    target.write(content)

source.close()
target.close()

#!/bin/bash -x
# создаем папки года и подпапки месяца
mkdir -p 20{10..17}/{01..12}
for i in 20{09..17}
do
          #в цикле обходим месяцы
           for j in {01..12}
              do
          #создаем файлы и копируем в папки
              touch {01..12}.txt
               mv $j.txt $i/$j
          done
          # проходимся по файлам и добавляем название файл** в файл.
          for t in {01..12}.txt
          do
              echo файл$t | sed 's/.txt*/ /'> $t #удаляем .txt из файлов
          done
done

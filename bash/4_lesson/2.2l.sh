#!/bin/bash -x
# создаем папки года и подпапки месяца
mkdir -p 20{10..17}/{1..12}
for i in {2010..2017}
do
    #в цикле обходим месяцы
           for j in {1..12}
              do
                  #создаем файлы и копируем в папки
              touch {1..12}.txt; tee -a $j.txt
               cp $j.txt $i/$j
          done
done

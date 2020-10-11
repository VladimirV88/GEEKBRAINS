#!/bin/bash
for f in *
do
        # если копия .bak есть, то будем читать следующий файл
    if [ -f ${f}.bak ]
    then
        echo "Skiping $f file..."
        continue  # переходим к следующей итерации
    fi
        # архива нет, копируем
    /bin/cp $f $f.bak
done

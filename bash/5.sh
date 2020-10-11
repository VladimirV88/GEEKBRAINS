#/bin/bash
if [ $# -lt 3 ]
then
                     echo Программа создает на указанный файл жесткую и символическую ссылку
                     echo Формат использования
                     echo $0 original_file hardlink_name sofftlink_name
                     exit 1
fi
original_file=$1
hardlink_name=$2
softlink_name=$3
echo Создаем
ln $original_file $hardlink_name
ln -s $original_file $softlink_name

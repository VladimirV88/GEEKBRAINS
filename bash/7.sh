#!/bin/bash
#Прочитаем с клавиатуры a и b
echo "Введите a: "
read a
echo "Введите b: "
read b
let "c = a + b"  #сложение
echo "a+b= $c"
let "c = a * b"  #умножение
echo "a*b= $c"
let "c = a ** b" #возведение в степень
echo "a^b= $c"
let "c = a / b"   #деление
echo "a/b= $c"
let "c <<= 2"    #сдвигает c на 2 разряда влево
echo "c после сдвига на 2 разряда: $c"
let "c = a % b" # находит остаток от деления a на b
echo "$a / $b. остаток: $c "
let "a +=5" #увеличить на 5
echo $a
let "a *=5" #умножить а на 5
echo $a

#/bin/bash
[ $# -lt 3 ]&&{
                     echo Параметров не может быть меньше трех
                     echo Формат использования
                     echo $0 arg1 arg2 arg3
                     exit 1
}

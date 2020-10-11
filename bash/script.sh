#!/bin/bash -x
if [ -e file50 ]
then
    echo "true"
else
    touch file50
fi

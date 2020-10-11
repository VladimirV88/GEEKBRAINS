#!/bin/bash -x
dir=$1
if [-z $dir]
then
    echo "error"
    exit
else
    mkdir $dir
fi

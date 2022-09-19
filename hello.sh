


#!/bin/sh
echo "hello world"
read -p 'Who am I? ' x

whereami=$(pwd)
echo "I am $x: you are in the ${whereami} folder"

arg1=$1
arg2=$2


echo "argument 1 = ${arg1}"
echo "argument 1 = ${arg2}" 

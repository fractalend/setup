#!/bin/bash


for x in $(ls -A); do 
    if  grep  -v -E '^\.(git)'  <<< $x | grep  -q -E '^\.'  ;  then
        ln -s $(pwd)/$x ../$x 
    fi
    #echo "$x.test"
    done

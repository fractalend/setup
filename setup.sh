#!/bin/bash

for x in $(ls -A); do 
    if  grep  -v -E '^\.(git)'  <<< $x | grep  -q -E '^\.'
      then
        if  [[ -e "../$x" || -h "../$x" ]]
            then 
                rm -rf ../$x
        fi 
        ln -s $(pwd)/$x ../$x 
    fi
done

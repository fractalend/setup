#!/bin/bash

for x in $(ls -A); do 
    if  grep  -v -E '^\.(git)'  <<< $x | grep  -q -E '^\.'
      then
        if  [[ -f "../$x" || -d "../$x" ]]
            then 
                rm -rf ../$x
        fi 
        ln -s $(pwd)/$x ../$x 
    fi
done

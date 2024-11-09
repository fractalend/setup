#!/bin/python3
import time
import sys
import os

if(len(sys.argv) != 2 or not isinstance(int(sys.argv[1]), int)):
    print("Usage: session.py <Number of Minutes>");
    exit();

alert = "notify-send -a \"Session End\" STOP "
print(f'started at  {time.ctime()}');
minutes = int(sys.argv[1]);
time.sleep(minutes*60);
for i in range(3):
    print("▄▄▄▄▄▄▄▄▄▄▄", end=" ", flush=True);
    time.sleep(1);
print('\n');
os.system(alert);









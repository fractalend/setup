#!/bin/python3
import time
import sys
import os

if(len(sys.argv) != 2 or not isinstance(int(sys.argv[1]), int)):
    print("Usage: break <Number of Minutes>");
    exit();

alert = "gedit stop_msg"
print("Start");
minutes = int(sys.argv[1]);
time.sleep(minutes*60);
for i in range(3):
    print("▄▄▄▄▄▄▄▄▄▄▄", end=" ", flush=True);
    time.sleep(1);
print('\n');
os.system(alert);









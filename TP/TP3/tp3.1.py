import os
import signal
import sys
import time

i = 0

def appel(numero, frame):
    global i
    i += 1
    if i == 1:
        print("interruption 1")
    elif i == 2:
        print("interruption 2")
    elif i == 3:
        print("interruption 3")
    elif i == 6:
        sys.exit(1)

signal.signal(signal.SIGINT, appel)

while True:
    print("Je suis vivant, mon PID est", os.getpid())
    time.sleep(1)
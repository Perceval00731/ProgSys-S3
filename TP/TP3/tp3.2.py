import os
import signal
import sys
import time

pid = os.fork()

def finfils(numero,frame):
    print("reception signal: ",numero)
    status = os.wait()
    print("PID du fils termine ", status[0])
    print("code de retour ", status[1])



if pid: #pere
    signal.signal(signal.SIGCHLD,finfils)
    i=0
    while True:
        print("je suis le pere, mon PID est: ", os.getpid()," le compteur est de: ",i)
        i+=1
        time.sleep(3)

else: #fils
    print("je suis le fils, mon PID est: ", os.getpid())
    time.sleep(20)
    os._exit(3)
    
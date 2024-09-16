import os,signal,time,sys

#pid=os.fork()

#exo 2
#if pid == 0:
#    args=["xeyes"]
#    os.execvp(args[0],args)
#    #cmd="xeyes"
#    #os.execl(cmd,cmd)
#else:  
#    print("Je suis le père")
#    os.wait()
#    print('termine')


#exo3


def erreur(signum,frame):
    print("le signal reçu est: ",signum)

signal.signal(signal.SIGTERM,erreur)
for i in range(10):
    print("je suis vivant mon PID est: ",os.getpid())
    time.sleep(2)


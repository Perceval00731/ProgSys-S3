from os import *
from sys import argv

try:
    if len(argv)<=1:
        write(2,b"missing argument\n")
        exit(1)
    
    #lire le fichier
    fd=open(argv[1],O_RDONLY)
    buffer=read(fd,256)
    while len(buffer)>0:
        write(1,buffer)
        buffer=read(fd,256)
    close(fd)

except OSError as e:
    print("system call error",e.strerror)
    exit(1)
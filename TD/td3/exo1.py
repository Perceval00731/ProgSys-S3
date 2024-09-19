#! /usr/bin/env python3
from os import *
from sys import argv

try:
    if len(argv)<=1:
        write(2,b"missing argument\n")
        exit(1)

    fd=open(argv[1],O_WRONLY)
    write(fd,bytes(argv[1],"utf-8"))
    close(fd)

except OSError as e:
    print("system call error",e.strerror)
    exit(1)

#exo 1
#erreur car nous n'avons pas les droits d'ecriture sur le fichier

#exo 2
#erreur car le fichier n'existe pas et on a pas precise CREAT

#exo 3
#cela va creer le fichier exo1.none et ecrire dedans le nom du fichier mais ne pourra plus le modifier ensuite

#exo 4
#cela va fonctionner mais que si le fichier exo1 n'existe pas deja

#exo 5

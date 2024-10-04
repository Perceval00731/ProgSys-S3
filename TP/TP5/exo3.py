import os
import sys
import random
import time
import string

# Créer un pipe
rd, wd = os.pipe()
rd2, wd2 = os.pipe()

# Forker le processus
pid1 = os.fork()
pid2 = os.fork()

if pid1 == 0:  # fils 1
    x,y = random.randint(1, 100), random.randint(1, 100)
    print(f"Processus 1 nombres: x={x}, y={y}")
    os.write(wd, f"{x} {y}".encode())
    os.close(wd)

    a,b = os.read(rd2, 1024).decode().split()
    print(f"Processus 1 lettres: a={a}, b={b}")
if pid2==0:
    x,y = os.read(rd, 1024).decode().split()
    x,y = int(x), int(y)
    print(f"Processus 2 nombres: x={x}, y={y}")
    a,b= random.choice(string.ascii_letters), random.choice(string.ascii_letters)
    print(f"Processus 2 lettres: a={a}, b={b}")
    os.write(wd2, f"{a} {b}".encode())
    os.close(wd2)
else:
    print("Processus père")
    os.waitpid(pid1, 0)
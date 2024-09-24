import os

# Créer un pipe
r, w = os.pipe()

# Forker le processus
pid = os.fork()

if pid == 0:  # Processus enfant
    os.close(r)  
    os.write(w, b'2024') 
    os.close(w) 
else:  # Processus parent
    os.close(w) 
    os.waitpid(pid, 0)
    sortie = os.read(r, 1024)
    os.close(r)
    print(sortie.decode())

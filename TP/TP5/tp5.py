import os
import sys

# Créer un pipe
rd, wd = os.pipe()

# Forker le processus
pid = os.fork()

if pid == 0:  # Processus enfant
    os.close(wd)  # Fermer le descripteur d'écriture
    message = os.read(rd, 1024)  # Lire le message depuis le pipe
    os.close(rd)  # Fermer le descripteur de lecture
    print("Message reçu par le fils:", message.decode())  # Afficher le message
else:  # Processus parent
    os.close(rd)  # Fermer le descripteur de lecture
    message = "Bonjour du processus père"
    os.write(wd, message.encode())  # Écrire le message dans le pipe
    os.close(wd)  # Fermer le descripteur d'écriture
    os.waitpid(pid, 0)  # Attendre la fin du processus enfant
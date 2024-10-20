import os
import sys

if len(sys.argv) != 2:
    os.write(2, "Usage: python3 script.py <nom_fichier>\n".encode()) #sortie 2 pour les erreurs
    os._exit(1)

nom_fichier = sys.argv[1]
try:
    fd = os.open(nom_fichier, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

except OSError as e:
    os.write(2,"Erreur lors de l'ouverture du fichier: {e.strerror}".encode())
    os._exit(1)
os.write(1,"Entrez le texte à écrire puis tapez Ctrl-D pour terminer:\n".encode())

try:
    while True:
        data = os.read(0, 1024)
        if not data:
            break
        os.write(fd, data)
    
    os.close(fd)
    os._exit(0)
except OSError as e:
    os.write(2, "Erreur de lecture".encode())
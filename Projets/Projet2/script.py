import os
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <nom_du_fichier>")
    sys.exit(1)
nom_du_fichier = sys.argv[1]
try:
    fd = os.open(nom_du_fichier, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
except OSError as e:
    print(f"Erreur lors de l'ouverture du fichier: {e.strerror}")
    sys.exit(1)
os.write(1,"Entrez le texte à écrire puis tapez Ctrl-D pour terminer:\n".encode())

try:
    while True:
        data = os.read(0, 1024)
        if not data:
            break
        os.write(fd, data)
except OSError as e:
    print(f"Erreur lors de la lecture/écriture: {e.strerror}")
finally:
    os.close(fd)
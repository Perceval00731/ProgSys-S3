import os

# Chemin du fichier de sortie
chemin_fichier = 'sortie.txt'

# Ouvrir le fichier en écriture
f = os.open(chemin_fichier, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

# Rediriger la sortie standard vers le fichier
os.dup2(f, 1)
os.close(f)

# Créer un pipe
r, w = os.pipe()

# Forker le processus
pid = os.fork()

if pid == 0:  # Processus enfant
    os.close(r)  # Fermer le descripteur de lecture
    os.write(w, b"coucou")  # Écrire "coucou" dans le pipe
    os.close(w)  # Fermer le descripteur d'écriture
else:  # Processus parent
    os.close(w)  # Fermer le descripteur d'écriture
    sortie = os.read(r, 1024)  # Lire depuis le pipe
    os.close(r)  # Fermer le descripteur de lecture
    print(sortie.decode())  # Afficher le contenu lu
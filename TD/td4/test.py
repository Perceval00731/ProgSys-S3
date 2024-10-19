import os

chemin = 'sortie.txt'

os.dup2(os.open(chemin, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), 1)

print("cheffff")
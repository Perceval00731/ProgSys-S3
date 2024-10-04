import os
import time
import string
import random

# Chemin du tube nommé
tube_path = '/tmp/mon_tube'

# Ouvrir le tube en écriture
with open(tube_path, 'w') as tube:
    while True:
        lettreAleatoire = random.choice(string.ascii_letters)
        print(f"Écrivain : envoi de la lettre {lettreAleatoire}")
        tube.write(lettreAleatoire + '\n')
        tube.flush()
        time.sleep(1)
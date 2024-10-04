import os

# Chemin du tube nommé
tube_path = '/tmp/mon_tube'

# Ouvrir le tube en lecture
with open(tube_path, 'r') as tube:
    while True:
        lettre = tube.readline().strip()
        if lettre:
            print(f"Lecteur : lettre reçue {lettre}")
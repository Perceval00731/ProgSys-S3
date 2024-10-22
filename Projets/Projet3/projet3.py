import os
import signal
import time
import sys

# Liste des processus prêts
liste_processus = []
processus_actuel = 0

def fin_programme(signum, frame):  # tue tous les processus et quitte
    os.write(1, b"Fin du programme\n")
    global liste_processus
    for pid in liste_processus:
        os.kill(pid, signal.SIGKILL)
    sys.exit(0)

def creation_processus(signum, frame):
    global liste_processus

    pid = os.fork()
    if pid == 0:  # fils
        os.kill(os.getpid(), signal.SIGSTOP)  # Suspend le processus enfant immédiatement
        while True:
            os.write(1, f"Processus {os.getpid()} en cours d'exécution\n".encode())
            time.sleep(3)
    else:  # père
        liste_processus.append(pid)
        print("Liste des processus après ajout :", liste_processus)
        if len(liste_processus) == 1:
            # Démarrer le premier processus immédiatement
            os.kill(liste_processus[0], signal.SIGCONT)
            signal.alarm(15)

def changement_processus(signum, frame):
    global processus_actuel
    global liste_processus

    if liste_processus:
        # Arrêter le processus actuel
        print(f"Arrêt du processus {liste_processus[processus_actuel]}")
        os.kill(liste_processus[processus_actuel], signal.SIGSTOP)

        # Passer au processus suivant
        processus_actuel += 1
        if processus_actuel >= len(liste_processus):
            processus_actuel = 0

        # Démarrer le nouveau processus
        print(f"Démarrage du processus {liste_processus[processus_actuel]}")
        os.kill(liste_processus[processus_actuel], signal.SIGCONT)

        # Réarmer l'alarme pour 15 secondes
        signal.alarm(15)

# Initialiser les gestionnaires de signaux
signal.signal(signal.SIGINT, creation_processus)
signal.signal(signal.SIGALRM, changement_processus)
signal.signal(signal.SIGTERM, fin_programme)

print(f"PID du père : {os.getpid()}")
print("Utilisez 'kill -SIGINT <PID>' pour créer des processus")

# Boucle principale
while True:
    print("En attente de signal")
    time.sleep(100)

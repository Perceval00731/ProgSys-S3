import os
import signal
import time
import sys


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
        os.kill(os.getpid(), signal.SIGSTOP)  # on arrete le fils 
        while True:
            os.write(1, f"Processus {os.getpid()} en cours d'exécution\n".encode())
            time.sleep(3)

    else:  # père
        liste_processus.append(pid)
        message_ajout = f"Liste des processus après ajout : {liste_processus}\n"
        os.write(1, message_ajout.encode())
        if len(liste_processus) == 1:
            # on démarre le premier processus
            os.kill(liste_processus[0], signal.SIGCONT)
            signal.alarm(15)



def changement_processus(signum, frame):
    global processus_actuel
    global liste_processus

    if liste_processus:
        # on arrete le processus actuel
        message_arret = f"Arrêt du processus {liste_processus[processus_actuel]}\n"
        os.write(1, message_arret.encode())
        os.kill(liste_processus[processus_actuel], signal.SIGSTOP)
    
        # on change de processus
        processus_actuel += 1
        if processus_actuel >= len(liste_processus):
            processus_actuel = 0
    
        # on commence le nouveau processus
        message_demarrage = f"Démarrage du processus {liste_processus[processus_actuel]}\n"
        os.write(1, message_demarrage.encode())
        os.kill(liste_processus[processus_actuel], signal.SIGCONT)
    
        # on relance l'alarme
        signal.alarm(15)



# omodif gestionnaires de signaux
signal.signal(signal.SIGINT, creation_processus)
signal.signal(signal.SIGALRM, changement_processus)
signal.signal(signal.SIGTERM, fin_programme)


os.write(1, f"PID du père : {os.getpid()}\n".encode())
os.write(1, b"Utilisez 'kill -SIGINT <PID>' pour envoyer un signal qui va creer des processus\n")


# Boucle principale
while True:
    os.write(1, b"En attente de signaux\n")
    time.sleep(100)

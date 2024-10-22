import os
import signal
import time
import sys

# Liste des processus prêts
process_list = []
current_process = 0

def fin(signum, frame):
    os.write(1, b"Fin du programme\n")
    global process_list
    for pid in process_list:
        os.kill(pid, signal.SIGKILL)
    sys.exit(0)

def creation_process(signum, frame):
    global process_list

    pid = os.fork()
    if pid == 0: #fils
        # on suspend le processus fils
        os.kill(os.getpid(), signal.SIGSTOP)
        while True:
            print(f"Processus {os.getpid()} en cours d'exécution")
            time.sleep(3)

    else: #pere
        process_list.append(pid)
        print("Liste des processus après ajout :", process_list)
        if len(process_list) == 1:
            # Démarrer le premier processus immédiatement
            os.kill(process_list[0], signal.SIGCONT)
            signal.alarm(15)



def changement_process(signum, frame):
    global current_process
    global process_list

    if process_list:
        # Arrêter le processus actuel
        print(f"Arrêt du processus {process_list[current_process]}")
        os.kill(process_list[current_process], signal.SIGSTOP)

        # Passer au processus suivant
        current_process = (current_process + 1) % len(process_list)

        # Démarrer le nouveau processus
        print(f"Démarrage du processus {process_list[current_process]}")
        os.kill(process_list[current_process], signal.SIGCONT)

        # Réarmer l'alarme pour 15 secondes
        signal.alarm(15)


# Initialiser les gestionnaires de signaux
signal.signal(signal.SIGINT, creation_process)
signal.signal(signal.SIGALRM, changement_process)
signal.signal(signal.SIGTERM, fin)

print(f"PID du père : {os.getpid()}")
print("Utilisez 'kill -SIGINT <PID>' pour créer des processus")

# Boucle principale
while True:
    print("En attente de signal")
    time.sleep(100)

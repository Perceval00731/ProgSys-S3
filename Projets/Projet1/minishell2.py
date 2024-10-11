import os

cmd = input("$ ")
while cmd != "quit":
    args = cmd.split()
    if args[-1] == "&":
        args = args[:-1]
        background = True
    else:
        background = False
    
    pid = os.fork()
    if pid == 0: #enfant
        try:
            print(f"args: {args},   args[0]: {args[0]}")
            os.execvp(args[0], args)
        except OSError as e:
            print(f"Erreur d'exécution de la commande: {e.strerror}")
            os._exit(1)

    else: #parent
        if not background:
            status = os.waitpid(pid, 0)[1]
            print(f"Commande {cmd} executée premier plan avec le PID: {pid}, Code de retour: {os.WEXITSTATUS(status)}")
        else:
            print(f"Commande en arrière-plan avec PID: {pid}")

    cmd = input("$ ")
import os
import shlex

def execute_command(command):
    try:
        args = shlex.split(command)
        
        # Vérifier si la commande doit être exécutée en arrière-plan
        if args[-1] == '&':
            args = args[:-1]
            background = True
        else:
            background = False
        
        pid = os.fork()
        
        if pid == 0:  # Processus enfant
            try:
                os.execvp(args[0], args)
            except OSError as e:
                print(f"Erreur d'exécution de la commande: {e.strerror}")
                os._exit(1)
        else:  # Processus parent
            if not background:
                _, status = os.waitpid(pid, 0)
                print(f"PID: {pid}, Code de retour: {os.WEXITSTATUS(status)}")
            else:
                print(f"Commande exécutée en arrière-plan avec PID: {pid}")
    except OSError as e:
        print(f"Erreur de fork: {e.strerror}")

def main():
    while True:
        try:
            # Lire la ligne de commande
            command = input("myshell> ")
            
            # Quitter le shell si la commande est "exit"
            if command.strip().lower() == "exit":
                break
            
            # Exécuter la commande
            execute_command(command)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nPour quitter, tapez 'exit'.")

if __name__ == "__main__":
    main()
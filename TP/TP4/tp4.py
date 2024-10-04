from os import *
import traceback
import sys

try:
    fs=open(fSource, O_RDONLY)
    fd=open(fDest, O_WRONLY|O_CREAT|O_CREAT, 0o644)

except OSError as e:
    print("Erreur d'ouverture du fichier")
    print(traceback.format_exc())
    sys.exit(1)
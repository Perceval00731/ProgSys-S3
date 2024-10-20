import os
import sys


rd, wd = os.pipe()

pid1 = os.fork()

if pid1 == 0: # 1er fils
    os.dup2(wd, 1)
    os.close(rd)
    os.close(wd)
    os.execvp("ls", ["ls", "-l"])
    sys.exit(1)

pid2 = os.fork()

if pid2 == 0: # 2e fils
    os.dup2(rd, 0)
    os.close(rd)
    os.close(wd)
    os.execvp("grep", ["grep", "\\.py"])
    sys.exit(1)



os.close(rd)
os.close(wd)

os.waitpid(pid1, 0)
os.waitpid(pid2, 0)
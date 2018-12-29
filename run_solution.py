import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < solution.txt".format(sys.executable))
print(p)

#Note: Once the music has finished, the results will execute.
#Meanwhile, please wait for about 22 seconds.  

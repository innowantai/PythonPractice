import subprocess
import os


# =============================================================================
# subprocess.call('start', shell=True)
# =============================================================================


path = os.getcwd()
path = os.path.split(path)[0]



subprocess.run(["ls", "-l"])




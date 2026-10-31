import subprocess
import sys


def instalar_requirements():

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])


instalar_requirements()
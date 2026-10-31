import subprocess

def p(host):
    subprocess.run(['ping', host])
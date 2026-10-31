import random
import ipaddress

def gerar_ip():
    while True:
        ip = ipaddress.ip_address(random.getrandbits(32))

        if ip.is_global:
            return str(ip)
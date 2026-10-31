import os
import time
import platform
import sys
from halo import Halo
from colorama import Fore,Style
from modules.ping import p
from modules.gen_ip import gerar_ip
from modules.scanner import scan
from modules.check import instalar_requirements

instalar_requirements()

if platform.system() == "Windows":
    os.system("cls")
    os.system("title NETTOOLS")
else:
    os.system("clear")

def c():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

aa = Halo(text='Aguarde iniciando!', spinner='dots')

aa.start()

time.sleep(4)

aa.succeed('ok!')
c()
print(Fore.RED+'''
═══════════════════════════════════════════════
            NetTools - TERMOS DE USO
═══════════════════════════════════════════════

Para continuar, é necessário aceitar os
Termos de Uso do NetTools.

Ao prosseguir, você declara que leu,
compreendeu e concorda com todas as condições
de utilização da aplicação.

Digite [S] para aceitar ou [N] para cancelar.
'''+Style.RESET_ALL)

accept = input(Fore.RED+'S/N: '+Style.RESET_ALL)
time.sleep(2)

if accept.upper() == 'S':
    print(':)')
else:
    c()
    sys.exit()

c()

infor_system = platform.uname()

while True:
    try:
        print(Fore.RED+'======================================================================================'+Style.RESET_ALL)
        print(Fore.RED+ f'{infor_system.system}', Fore.RED+f'{infor_system.release}', Fore.RED+f'{infor_system.machine}', Fore.RED+'version 1.0'+Style.RESET_ALL)
        print(Fore.RED+'''
 __    _  _______  _______  _______  _______  _______  ___      _______ 
|  |  | ||       ||       ||       ||       ||       ||   |    |       |
|   |_| ||    ___||_     _||_     _||   _   ||   _   ||   |    |  _____|
|       ||   |___   |   |    |   |  |  | |  ||  | |  ||   |    | |_____ 
|  _    ||    ___|  |   |    |   |  |  |_|  ||  |_|  ||   |___ |_____  |
| | |   ||   |___   |   |    |   |  |       ||       ||       | _____| |
|_|  |__||_______|  |___|    |___|  |_______||_______||_______||_______|
        '''+Style.RESET_ALL)
        print(Fore.RED+'======================================================================================'+Style.RESET_ALL)
        print('[1] Ping', '[2] Generate IP', '[3] Scanner', '[4] Exit', sep='   ')

        s = input(Fore.RED+'$>: '+Style.RESET_ALL)

        if s == '1':
            c()
            print('''
            para descobrir o ip do site, digite o site abaixo pra podelo testar
                exemplo exmaplo.com sem o https:// ou https 
            ''')
            host = input('$>: ')
            p(host)
            time.sleep(2)
            c()
        elif s == '2':
            c()
            print('''
            Aguarde gerar o ip
            quando o ip estive disponivel copie
            ''')
            gen_a = Halo(text='Aguarde', spinner='dots')

            gen_a.start()
            time.sleep(5)
            gen_a.succeed('Iniciado!')

            gen_b = Halo(text='Gerando IP!', spinner='dots')

            gen_b.start()
            time.sleep(3)
            
            gen_b.succeed('Gerado com sucesso!')

            ip = gerar_ip()
            print(ip)
            time.sleep(6)
            c()
        elif s == '3':
            c()
            scan()
            input('Precione qualquer tecla pra voltar')
            c()
        elif s == '4':
            c()
            break
        else:
            print('Digite uma opção valida!')
            c()
    except Exception as erro:
        print("Erro:", erro)
        input("Enter para continuar...")
        c()

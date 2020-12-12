# e

import os
import sys
import time
import socket
import requests
from colorama import Fore

def __target__():
    time.sleep(1)
    clear = input(Fore.RED + "\n[!] ~ Are Clear Text In Terminal (y , n) ==>  ")
    if clear.lower() == "y":
        time.sleep(1)
        os.system("clear")
    if clear.lower() == "n":
        print("")
    if clear == "" or None:
        try:
            print(Fore.RED + "\n[!] Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass

    time.sleep(1)
    print( Fore.BLUE + "[*]"+ Fore.YELLOW +" ~ " + Fore.GREEN + "So . Pleass 3 Sec Wail ;)")
    time.sleep(3)
    wp = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " +Fore.GREEN + "Are You Target Is WordPress ? ( 1 : yes | 2: no )" + Fore.YELLOW + " ==>  ")
    if wp == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if wp == "1":
        time.sleep(1)
    if wp == "2":

            time.sleep(1)
            print(Fore.RED + "\n[" + Fore.BLUE + "!" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.YELLOW + "Error : Your Target Is Not WordPress ;(")
            time.sleep(1)
            sys.exit()


    #----
    clear2 = input(Fore.RED + "\n[!] ~ Are Clear Text In Terminal (y , n) ==>  ")
    if clear2 == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if clear2.lower() == "y":
        time.sleep(1)
        os.system("clear")
        
    if clear2.lower() == "N":
        time.sleep(1)
        print("")
  

    # ----
    #       /wp-content/plugins/
    time.sleep(1)
    target = input(Fore.RED + "\n[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "Pleass Enter Your Address Target" + Fore.YELLOW + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    m = requests.get("http://" + target + "/wp-content/plugins/")
    if m.status_code == 404 or m.status_code == 500:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Sory , Your Target Is Not WordPreass ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    else:
        time.sleep(1)
        print(Fore.GREEN + "\n[+]" + Fore.BLUE + " ~ " + Fore.GREEN + "Ok , Your Target Is WordPreass :)\n")
        time.sleep(0.2)
    # ------
    my_list = ["xmlrpc"]
    for i in my_list:
        time.sleep(0.1)
        test = requests.get("http://" + target + "/wp-content/plugins/" + i)
        if test.status_code == 404 or test.status_code == 500:
            try:
                time.sleep(1)
                print(Fore.RED + "[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Xmlrpc Target Is Close ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        if test.status_code != 404 or test.status_code != 500:
            time.sleep(1)
            print(Fore.GREEN + "[+]" + Fore.BLUE + " ~ " + Fore.GREEN + "Ok , Your Xmlrpc Target Is Open ;)")
__target__()

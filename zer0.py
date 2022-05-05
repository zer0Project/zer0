# Imports
import os
from time import sleep
from getpass import getpass

# Vars
users = {
    'fresh': 'root',
}

class Colors:
    BLACK = '\u001b[30m'
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"

# Funcs
os.system('clear')

def baish_banner():
    print(Colors.CYAN)
    print("""
                            -------------
                             Baish baish
    _._     _,-'""`-._      -------------
    (,-.`._,'(       |\`-/|  /
        `-.-' \ )-`( , o o) /
              `-    \`_`"'-
    """)
    print(Colors.RESET)

# Login panel
print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Initializing, please wait...")
sleep(1)
os.system("clear")

baish_banner()

Login = input(Colors.RED + ' Login: ' + Colors.RESET) 
Passwdd = getpass(Colors.RED + ' Password: '+ Colors.RESET)
print('')
print('')
if Login in users and Passwdd == users[Login]:
    print(Colors.GREEN + ' Login successful!'+ Colors.RESET)
else:
    print(Colors.RED + ' User or password is incorrect, try again.' + Colors.RESET)

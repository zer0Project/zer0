# Imports
import os
import requests
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

def after_login():
    print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Welcome: "+Login)
    print("")
    print(Colors.RED+' -----------------------')
    print(Colors.GREEN+' Welcome to zero Tools')
    print(Colors.RED+' -----------------------')
    print(Colors.RED+'      ^__^\ ')
    print(Colors.RED+'      (oo)\_______  ')
    print(Colors.RED+'      (__)\       )\/\ ')
    print(Colors.RED+'         ||----w | ')
    print(Colors.RED+'         ||     || ')
    print(Colors.RESET+"")
    print('')
    print(" ["+Colors.CYAN+"1"+Colors.RESET+"] Sms spoofing")
    print("")

def mobile_phone():
    print('  __i ')
    print(' |---|   ') 
    print(' |[_]|   ') 
    print(' |:::|    ')
    print(' |:::|    ')
    print('  \   \   ')
    print('   \_=_\ ')
    print(''+Colors.RESET)
    print('')
    print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] zer0 SMS Spoofer panel")
    print("")

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
    sleep(1)
    os.system('clear')
    baish_banner()
    Choice = input(" Select your choice: ")
    if Choice == "1":
        os.system("clear")
        mobile_phone()
        Region = input(" Region (Without +): ")
        if "+" in Region:
            os.system("clear")
            print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.RED+"-"+Colors.RESET+"] You put a +, closing ...")
            sleep(1)
            os.system("clear")
        else:
            Number = input(" Number: ")
            Message = input(" Message: ")
            if Message:
                resp = requests.post('https://textbelt.com/text', {
                    'phone': "+"+Region+Number,
                    'message': Message,
                    'key': 'textbelt'
                })
                os.system("clear")
                print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Sended to: "+Number)
                print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Message: "+Message)
                print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Closing in 5 seconds...")

                print("")
                
                if not resp.json()['success'] and resp.json()['error']:
                    print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.RED+"-"+Colors.RESET+"] You have reached your limit for today, closing ...")
                    sleep(5)
                    os.system("clear")
                else:
                    print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Sended...")
                    sleep(5)
                    os.system("clear")
    else:
        os.system('clear')
        print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"-"+Colors.RESET+"] Invalid choice!")

else:
    print(Colors.RED + ' User or password is incorrect, try again.' + Colors.RESET)

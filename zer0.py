# Imports
import os
from time import sleep

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

def login_banner():
    print("""
             """+Colors.RED+""",----------------,              ,---------,
        """+Colors.GREEN+""",-----------------------,          ,"        ,"|
      """+Colors.YELLOW+""","                      ,"|        ,"        ,"  |
     """+Colors.BLUE+"""+-----------------------+  |      ,"        ,"    |
     """+Colors.MAGENTA+"""|  .-----------------.  |  |     +---------+      |
     """+Colors.CYAN+"""|  |                 |  |  |     | -==----'|      |
     """+Colors.WHITE+"""|  |  C:\>Enter user |  |  |     |         |      |
     """+Colors.RED+"""|  |  C:\>Enter pass |  |  |/----|`---=    |      |
     """+Colors.GREEN+"""|  |  C:\>Loading... |  |  |   ,/|==== ooo |      ;
     """+Colors.YELLOW+"""|  |                 |  |  |  // |(((( [33]|    ,"
     """+Colors.BLUE+"""|  `-----------------'  |," .;'| |((((     |  ,"
     """+Colors.MAGENTA+"""+-----------------------+  ;;  | |         |,"     -zer0 Cheats-
        """+Colors.CYAN+"""/_)______________(_/  //'   | +---------+
   """+Colors.WHITE+"""___________________________/___  `,
  """+Colors.RED+"""/  oooooooooooooooo  .o.  oooo /,   \,"-----------
 """+Colors.GREEN+"""/ ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
"""+Colors.YELLOW+"""/_==__==========__==_ooo__ooo=_/'   /___________,"
"""+Colors.BLUE+"""`-----------------------------'
    """)
    print(Colors.RESET)

# Login panel
print(" ["+Colors.RED+"zer0"+Colors.RESET+"] ["+Colors.GREEN+"+"+Colors.RESET+"] Initializing, please wait...")
sleep(1)
os.system("clear")

login_banner()

Login = input(Colors.RED + ' Login: ' + Colors.RESET) 
Passwdd = getpass(Colors.RED + ' Password: '+ Colors.RESET)
print('')
print('')
if Login in users and Passwdd == users[Login]:
    print(Colors.GREEN + ' Login successful!'+ Colors.RESET)
else:
    print(Colors.RED + ' User or password is incorrect, try again.' + Colors.RESET)

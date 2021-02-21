try:
    from instabot import Bot
except ModuleNotFoundError:
    print('Run Following Command \n\n python -m pip install instabot \n\n')
    exit()

from pathlib import Path
from shutil import rmtree
from tqdm import tqdm
from getpass import getpass
import random
import json
import os


try: rmtree(str(Path(__file__).parent) + '/config/')
except: pass

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
color = random.choice(colors)


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    clr()
    logo = '''

         __                   __           __  
         )_)  _        _   )  )_)  _   _  (_ ` 
        / \  (_) (_(  (_( (  /__) (_) (  .__)  
                   _)                 _)       

    '''
    print(color,logo)


def login():
    try:
        with open('creds','r') as f:
            d = json.loads(f.read())
            username = d['username']
            password = d['password']
            bot.login(username=username,password=password)
            return True
    except FileNotFoundError:
        username = input('Enter your Username: ')
        password = getpass('Enter your Password: ')
        d = {'username':username,'password':password}
        with open('creds','w') as f:
            f.write(json.dumps(d))
        return login()

def spam():
    banner()
    bot.delays["message"] = 0
    victim = input('Username : ')
    no_of_msgs = int(input('No. of Messages : '))

    option = input('Message Type? \n 1: Specific Message \n 2: Counting \n Your Choice: ')

    if option == '1':
        msg = input('Your Message: ')
        for i in tqdm(range(no_of_msgs),desc="Messaging..."):
            bot.send_message(msg,bot.get_user_id_from_username(victim))
    elif option == '2':
        for i in tqdm(range(no_of_msgs),desc="Messaging..."):
            bot.send_message(str(i+1),bot.get_user_id_from_username(victim))


def options():
    banner()

    print('0 : Exit')
    print('1 : Logout')
    print('2 : Spam')

def get():
    num = int(input('Enter Your Choice: '))
    if num == 0:
        exit()
    elif num == 1:
        bot.logout()
    elif num == 2:
        spam()


banner()
bot = Bot()
login()

while True:
    options()
    get()
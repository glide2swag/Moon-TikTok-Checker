import os
import time
from pypresence import Presence

try:
    import aiohttp
except ImportError:
    os.system('python -m pip install aiohttp')

try:
    import colorama
except ImportError:
    os.system('python -m pip install colorama')

import random
import getpass
import string
import asyncio
import aiohttp
from time import sleep
from colorama import Fore
from os import system

system('cls')
system("title " + 'Moon Checker')

client_id = "922549349878222888"
rpc = Presence(client_id)
rpc.connect()

rpc.update(state="v1",details="Checking Users",large_image="moon2",large_text="Checking Users",small_text="by @szay",small_image="moon3",start=time.time())

class Checker:

    def __init__(self):
        self.names = []
        self.real_amount_names = ''
        self.amount_names = ''
        self.o = 0
        self.p = 0
        self.available = []
        self.username = getpass.getuser()
        self.magenta = Fore.MAGENTA
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.head = Fore.MAGENTA + f' [{Fore.YELLOW + "-" + Fore.BLUE}]'

    def contents(self, letters, num):
        while True:
            amount_names = input(self.magenta + f'{self.head}    How many: ')
            if amount_names.isalnum() is True:
                break
            else:
                print(self.red + f'{self.head}{self.red}    Invalid option!')
        x = 0
        print(self.magenta + f'{self.head}    Generating Names...')
        while int(amount_names) > x:
            n = ''.join(random.choice(letters) for i in range(num))
            self.names.append(n)
            x += 1
        names = list(dict.fromkeys(self.names))
        for i in names:
            if i.isnumeric() is True:
                names.remove(i)
        self.real_amount_names = len(names)
        print(self.green + f'{self.head}{self.green}    Names Generated!')
        print(self.green + f'{self.head}{self.green}    Removed Invalid Names!')
        print(self.green + f'{self.head}{self.green}    Starting...')

    def save(self):
        while True:
            try:
                open(f'C:/users/{self.username}/Desktop/names.txt', 'x')
                break
            except FileExistsError:
                print(self.red + f'{self.head}{self.red}    File name already exists, rename or delete!')
                print(self.red + f'{self.head}{self.red}    Retrying!')
                sleep(3)
                continue
        while True:
            file_object = open(f'C:/users/{self.username}/Desktop/names.txt', 'a')
            for i in self.available:
                file_object.write(f"Username : {i}\n")
            file_object.close()
            break
        print(self.magenta + f'{self.head}    File saved in desktop!')
        sleep(3)

    async def main_checker(self, session: aiohttp.ClientSession, user):
        while True:
            async with session.head(url := f'https://www.tiktok.com/@{user}', ssl=False) as resp:
                if self.o >= int(self.real_amount_names):
                    while True:
                        file = input(self.magenta + f'{self.head}    Do you want to write the available'
                                                    ' names in a file? (y/n): ').lower()
                        if file == 'y':
                            self.save()
                            exit()
                        elif file == 'n':
                            while True:
                                leave = input(self.magenta + f'{self.head}    Press [ENTER] to exit!')
                                if leave == "":
                                    sleep(0.5)
                                    exit()
                        else:
                            print(Fore.RED + f'{self.head}{self.red}    Invalid option!')
                elif resp.status == 200:
                    print(self.head + f'{self.red}    {url} ─────── {user}')
                    system("title " + f'Moon Checker ~~ Tried {self.o + 1} Times ~~ {self.p}'
                                      f' Successful Attempts')
                    self.o += 1
                else:
                    print(self.head + f'{self.green}    {url} ─────── {user}'
                                      f'{self.green}                                                   [claimable]')
                    system("title " + f'Tiktok Name Checking Tool ~~ Tried {self.o + 1} Times ~~ {self.p}'
                                      f' Successful Attempts')
                    self.o += 1
                    self.p += 1
                    self.available.append(user)

    def random_generated(self):
        while True:
            try:
                amount_of_chars = input(self.magenta + f'{self.head}    Username Length: ')
                avail_length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                if int(amount_of_chars) in avail_length:
                    while True:
                        has_numbers = input(self.magenta + f'{self.head}    numbers? (y/n): ').lower()
                        if has_numbers == 'y':
                            self.contents(string.ascii_lowercase + string.digits, int(amount_of_chars))
                            self.tasks()
                        elif has_numbers == 'n':
                            self.contents(string.ascii_lowercase, int(amount_of_chars))
                            self.tasks()
                        else:
                            print(self.red + f'{self.head}{self.red}    Invalid option!')
                            continue
                else:
                    print(self.red + f'{self.head}{self.red}    Invalid option!')
                    continue
            except ValueError:
                print(self.red + f'{self.head}{self.red}    Invalid option!')
                pass

    def tasks(self):
        async def task1():
            async with aiohttp.ClientSession() as session:
                return await asyncio.gather(*[self.main_checker(session, user) for user in self.names])
        asyncio.get_event_loop().run_until_complete(task1())


print(Fore.RED + f'''
 ███▄ ▄███▓ ▒█████   ▒█████   ███▄    █                 
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █                 
▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒                
▒██    ▒██ ▒██   ██░▒██   ██░▓██▒  ▐▌██▒                
▒██▒   ░██▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░                
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒        v1          
░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░                
░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░                 
       ░       ░ ░      ░ ░           ░                 
                                                        
 ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░  

                                                                                                   ''')
checker = Checker()
checker.random_generated()


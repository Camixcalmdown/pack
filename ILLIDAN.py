import pystyle
import time
from pystyle import *
import requests
import sys
import os
import webbrowser
import urllib.parse
import platform

def open_link():
    url = "https://t.me/+BrrBWajXGDNiMDBi"
    system = platform.system()

    if system == "Linux":
        if "com.termux" in os.getenv("PREFIX", ""):
            os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        pass
open_link()



deanon = '''
Имя: Павел
Фамилия: Чермак
Отчество: Андреевич
Возраст: 36 лет
Дата рождения: 26.04.1988
Почта: pavelchermak@gmail.com
Пароль: 26041988A

time: 0.4
'''

COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}
menu = fr'''      
   

                              
                                                                                                                           
   
                                                                                  ▪
                                                                         
                                                  ▪          ▪        
  ▪          ▪                                                         ▪         
                                                                                                        ▪
 
  ▪                    ▄█   ▄█        ▄█        ▄█  ████████▄     ▄████████ ███▄▄▄▄   
                       ███  ███       ███       ███  ███   ▀███   ███    ███ ███▀▀▀██▄       ▪
                       ███▌ ███       ███       ███▌ ███    ███   ███    ███ ███   ███ 
                       ███▌ ███       ███       ███▌ ███    ███   ███    ███ ███   ███ 
            ▪          ███▌ ███       ███       ███▌ ███    ███ ▀███████████ ███   ███ 
                       ███  ███       ███       ███  ███    ███   ███    ███ ███   ███ 
                       ███  ███▌    ▄ ███▌    ▄ ███  ███   ▄███   ███    ███ ███   ███ 
                       █▀   █████▄▄██ █████▄▄██ █▀   ████████▀    ███    █▀   ▀█   █▀  
    ▪                  ▀         ▀                                                          ▪
                     ▪     
                                                                                       ▪
                                       
                                                                       ▪
                                                                                                ▪

                     ▪                        BETA 1.0.0
                                                   
                                       ○━━━━━━━━━━━━━━━━━━━━━━━○      ▪
                                       ┃ [1]  GLOBAL SEARCH    ┃
                                       ┃ [88]      MISC        ┃      
                                       ○━━━━━━━━━━━━━━━━━━━━━━━○     
                                                   

          

                                           
 '''
def searchbd():
    choose = input('\033[1;90mГлобальный Поиск>\n')
    data = {"token": "7629810639:i8ao3ZZj",
    "request": choose , 'limit': 1000, "lang":"ru", "type":"short"}
    url ='https://leakosintapi.com/'
    reponse = requests.post(url,json=data)
    print(reponse.json())
    input('')
    mainmenu()

def mainmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    grad_menu = Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(menu)) #ставьте свои цвета 
    print(grad_menu)                       #да тут только выше
    choose = int(input('\033[1;31mВыберите>\n'))
    if choose == 1:
      searchbd()
      input('')
      mainmenu()
    if choose == 2:
      searchbd()
      input('')
      mainmenu()
    if choose == 3:
      searchbd()
      input('')
      mainmenu()
    if choose == 4:
      searchbd()
      input('')
      mainmenu()
    if choose == 5:
      searchbd()
      input('')
      mainmenu()
    if choose == 6:
      searchbd()
      input('')
      mainmenu()
    if choose == 99:
      exit()
    if choose == 88:
     input('\033[36mПрограмма была сделана @vega4llov, Версия софта: BETA 1.0.0 \n') 
     mainmenu()

#основной код
mainmenu()
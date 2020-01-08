from urllib import request
import time
import pyautogui
import webbrowser
from linecache import getline

def type_speed():
    x = input("\n\n\t How fast want you type (number of chars per minute)  : ")
    try:
       y = int(x)
    except:
        raise TypeError("\n\n\t Your type speed should be a number!!!")
    else:
        return y

def tab_open(url):
    webbrowser.open_new_tab(url)
    resp = request.urlopen(url)
    a = resp.code
    while 1 < 2:
        if a == 200: break

def delay_calculate(speed):
    speed_per_sec = speed/60        #ilosc znakow na sekunde
    delay = 1 / speed_per_sec
    C = 0.685                          #jakaś stała która przybliży wynik
    return delay*C

def get_text():
    f=open("text.txt","r") #ilość lini
    s = getline('text.txt',1) 
    f.close()
    s.strip() #usuwa zew. spacje ze stringa
    return convert(s)
  
    
def convert(text):
    how_many_chars = len(text)
    tab_char=[]
    for x in range(0,how_many_chars):
        tab_char.append(text[x])
    return tab_char

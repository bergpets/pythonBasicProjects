# coding=utf-8
from pyfiglet import Figlet
import folium
import time, sys
import os

preview_text = Figlet(font='slant')
print(preview_text.renderText('TIMER 3000'))
while True:
    h = int(input("Часы: "))
    if h>24 or h<0:
        print("Error")
        break
    m = int(input("Минуты: "))
    if m>60 or m<0:
        print("Error")
        break
    s = int(input("Секунды: "))
    if s>60 or s<0:
        print("Error")
        break
    nSeconds = h*3600 + m*60 + s
    print("Осталось времени: ", end='')
    for n in range(nSeconds):
        if (nSeconds//3600)<10:
            newh = '0' + str(nSeconds//3600)
        else:
            newh = str(nSeconds//3600) 
        if (nSeconds//60%60)<10:
            newm = '0' + str(nSeconds//60%60)
        else:
            newm = str(nSeconds//60%60)
        if (nSeconds%60)<10:
            news = '0' + str(nSeconds%60)
        else:
            news = str(nSeconds%60)
        time.sleep(1)
        os.system('cls')
        print("Осталось времени: %s:%s:%s" % (newh, newm, news),end='\r')
        nSeconds -= 1
    print("Время вышло!")

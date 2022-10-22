from pyfiglet import Figlet
import folium
import random

preview_text = Figlet(font='slant')
print(preview_text.renderText('SUM OF DIGITS 3000'))
n = input("Ваше число: ")
n = list(n)
summ = 0
item = 0
for i in range(len(n)):
    n[i] = int(n[i])
    summ += n[i]
print(summ)
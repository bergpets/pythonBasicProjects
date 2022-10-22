from pyfiglet import Figlet
import folium
import random

preview_text = Figlet(font='slant')
print(preview_text.renderText('FRASE GENERATOR 3000'))

i = 1
j = 0
print("Стопслово: '+'")

listNoun = []
listVerb = []
el = "0"
while el != '+':
    el = input()
    if el != '+':
        listNoun.append(el)
        i += 1
el = "0"
while el != '+':
    el = input()
    if el != '+':
        listVerb.append(el)
        i += 1
el = "0"        
print(listNoun)
print(listVerb)

n = int(input("Количество фраз: "))
i = 0
#сгс,гсс,ссг
for i in range(n):
    comb = int(random.randint(1, 3))
    if comb == 1:
        print(random.choice(listNoun) + " " + random.choice(listVerb) + " " + random.choice(listNoun) + " ")
    elif comb == 2: 
        print(random.choice(listVerb) + " " + random.choice(listNoun) + " " + random.choice(listNoun) + " ") 
    elif comb == 3:
        print(random.choice(listNoun) + " " + random.choice(listNoun) + " " + random.choice(listVerb) + " ")
    i += 1
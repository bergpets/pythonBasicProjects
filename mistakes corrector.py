from pyfiglet import Figlet
import folium
import random

preview_text = Figlet(font='slant')
print(preview_text.renderText('MISTAKE CORRECTOR 3000'))

i = 1
print("Стопслово: '+'")
print("Введите проверяемые слова: ")
listRightWords = []
el = "0"

while el != '+':
    el = input()
    if el != '+':
        listRightWords.append(el)
        i += 1
el = "0"

strMistakes = input()
strMistakes = strMistakes.split(" ")
result = 0
for wordMistakes in strMistakes:
    for words in listRightWords:
        if len(wordMistakes) == len(words):
            for letterMistakes in range(len(wordMistakes)):
                if wordMistakes[letterMistakes] == words[letterMistakes]:
                    el += wordMistakes[letterMistakes]
                    result += 1
                elif wordMistakes[letterMistakes] != words[letterMistakes]:
                    el += " " + words[letterMistakes] + " "
            if len(wordMistakes) - result == 1:
                print(el)
            result = 0;
            el = ''
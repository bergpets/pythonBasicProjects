'''Задание 5 Иногда после работы хорошо бы собраться и поиграть с товарищами в “шахты и вертолеты” но иногда на создание персонажей уходит слишком много времени. Напишите “генератор персонажей” генерирующий
имя 
возраст 
класс апа
параметры (можно взять параметры из Fallouta) 
характеристики (можно взять SPECIAL из Fallouta) 
навыки/особенности (случайное количество)'''

from pyfiglet import Figlet
import folium
import random

preview_text = Figlet(font='slant')
print(preview_text.renderText('CHARACTER GENERATOR 3000'))

listName = ['Steve', 'Michael', 'Nigag', 'Aboba', 'Jopa', 'Batman', 'Tony Stark', 'Legenda', 'MORGENSHTERN', 'Smesharik']
listClass = ['Разведчик','Солдат','Поджигатель','Подрывник','Пулемётчик','Инженер','Медик','Снайпер','Шпион']
#age - random (18, 40)
listParametrs = ['Сила', 'Восприятие', 'Выносливость' , 'Привлекательность', 'Интеллект', 'Ловкость', 'Удача']
#parametrs dig - random (1,10)
listSpecial = ["'Легенда курилки' - +7 к Выносливости после применения на 10с", "'Писал все конспекты' - +7 к Интеллекту после применения на 5с", "'Убежать от Крапова' - +5 к Удаче и Ловкости после применения на 15с", "'Не хватает стульев в кабинете' - +5 к Силе после применения на 10с", "'Красивая первокурсница' - +7 к Привлекательности после применения на 20с", "'Божье благословение: Встретить Куджа' - +3 ко всем характеристикам после применения на 30с"]

while True:
    des = input("Сгенерировать нового персонажа?(y/n) ")
    if des == 'y':
        print("Ваш персонаж: ")
        name_text = Figlet(font='slant')
        print(name_text.renderText(random.choice(listName)))    
        print("Возраст: ", random.randint(18,40))
        print("Класс: ", random.choice(listClass))
        print("Характеристики:")
        for i in range(len(listParametrs)):
            print("\t" + listParametrs[i] + ":" + str(random.randint(1,4)))
        print("Special: ", random.choice(listSpecial))
    elif des == 'n':
        break
    else:
        print("Error")
        
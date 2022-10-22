'''������� 5 ������ ����� ������ ������ �� ��������� � �������� � ���������� � ������ � ���������� �� ������ �� �������� ���������� ������ ������� ����� �������. �������� ���������� ���������� ������������
��� 
������� 
����� ���
��������� (����� ����� ��������� �� Fallouta) 
�������������� (����� ����� SPECIAL �� Fallouta) 
������/����������� (��������� ����������)'''

from pyfiglet import Figlet
import folium
import random

preview_text = Figlet(font='slant')
print(preview_text.renderText('CHARACTER GENERATOR 3000'))

listName = ['Steve', 'Michael', 'Nigag', 'Aboba', 'Jopa', 'Batman', 'Tony Stark', 'Legenda', 'MORGENSHTERN', 'Smesharik']
listClass = ['���������','������','�����������','���������','���������','�������','�����','�������','�����']
#age - random (18, 40)
listParametrs = ['����', '����������', '������������' , '�����������������', '���������', '��������', '�����']
#parametrs dig - random (1,10)
listSpecial = ["'������� �������' - +7 � ������������ ����� ���������� �� 10�", "'����� ��� ���������' - +7 � ���������� ����� ���������� �� 5�", "'������� �� �������' - +5 � ����� � �������� ����� ���������� �� 15�", "'�� ������� ������� � ��������' - +5 � ���� ����� ���������� �� 10�", "'�������� �������������' - +7 � ����������������� ����� ���������� �� 20�", "'����� �������������: ��������� �����' - +3 �� ���� ��������������� ����� ���������� �� 30�"]

while True:
    des = input("������������� ������ ���������?(y/n) ")
    if des == 'y':
        print("��� ��������: ")
        name_text = Figlet(font='slant')
        print(name_text.renderText(random.choice(listName)))    
        print("�������: ", random.randint(18,40))
        print("�����: ", random.choice(listClass))
        print("��������������:")
        for i in range(len(listParametrs)):
            print("\t" + listParametrs[i] + ":" + str(random.randint(1,4)))
        print("Special: ", random.choice(listSpecial))
    elif des == 'n':
        break
    else:
        print("Error")
        
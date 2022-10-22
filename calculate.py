from pyfiglet import Figlet
import folium

preview_text = Figlet(font='slant')
print(preview_text.renderText('CALCULATOR 3000'))

print("��������: ")
print("'+'")
print("'-'")
print("'/'")
print("'*'")
print("'%'")
print("'^'")
print("'_' - ���������� �����")
print("��� ������: 'q'")

def summ(a, b):
    try:
        return a+b
    except:
        print("Error")
        return 0 
    
def diff(a, b):
    try:
        return a-b
    except:
        print("Error")
        return 0 
    
def mult(a, b):
    try:
        return a+b
    except:
        print("Error")
        return 0 
    
def div(a, b):
    try:
        return a/b
    except:
        print("Error")
        return 0 
    
def mod(a, b):
    try:
        return a%b
    except:
        print("Error")
        return 0 
    
def exp(a, b):
    try:
        return a**b
    except:
        print("Error")
        return 0 

def root(a, b):
    try:
        return a**(b**(-1))
    except:
        print("Error")
        return 0 

while(1):
    c = input("��������: ")
    a = float(input("������ �����: "))
    b = float(input("������ �����: "))
    
    if c == '+':
        print("���������: %.f" % summ(a,b), end="\n")
        
    elif c == '-':
        print("���������: %.f" % diff(a,b), end="\n")
         
    elif c == '/':
        print("���������: %.f" % div(a,b), end="\n")
        
    elif c == '*':
        print("���������: %.f" % mult(a,b), end="\n")      

    elif c == '%':
        print("���������: %.f" % mod(a,b), end="\n")
        
    elif c == '^':
        print("���������: %.f" % exp(a,b), end="\n")
        
    elif c == '_':
        print("���������: %.f" % root(a,b), end="\n")        
        
    elif c == 'q':
        break
    
    else:
        print("Error", end="\n")
        

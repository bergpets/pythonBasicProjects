from pyfiglet import Figlet
import folium

preview_text = Figlet(font='slant')
print(preview_text.renderText('CALCULATOR 3000'))

print("Операции: ")
print("'+'")
print("'-'")
print("'/'")
print("'*'")
print("'%'")
print("'^'")
print("'_' - извлечение корня")
print("Для выхода: 'q'")

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
    c = input("Операция: ")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    
    if c == '+':
        print("Результат: %.f" % summ(a,b), end="\n")
        
    elif c == '-':
        print("Результат: %.f" % diff(a,b), end="\n")
         
    elif c == '/':
        print("Результат: %.f" % div(a,b), end="\n")
        
    elif c == '*':
        print("Результат: %.f" % mult(a,b), end="\n")      

    elif c == '%':
        print("Результат: %.f" % mod(a,b), end="\n")
        
    elif c == '^':
        print("Результат: %.f" % exp(a,b), end="\n")
        
    elif c == '_':
        print("Результат: %.f" % root(a,b), end="\n")        
        
    elif c == 'q':
        break
    
    else:
        print("Error", end="\n")
        

#!C:/Users/zx22student3209/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\n")

x = input("Ingresa primer numero")
y = input("Ingresa segundo numero")
c=None
s=None

def sumar(a,b):
    c = (a + b)
    print(c)

def restar(a,b):
    c= (a - b)
    print(c)

def menu():
    print("Seleccione una operacion \n 1-Sumar \n 2-restar \n 3-Multiplicacion \n")
    s=input()

menu()





if s==1 :
    sumar(x,y)
    menu()

if s==2 :
    restar(x,y)
    menu()




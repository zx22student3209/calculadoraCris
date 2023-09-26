#!C:/Users/zx22student3209/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\n")

x = int(input("Ingresa primer numero =\n"))
y = int(input("Ingresa segundo numero =\n"))
c=None


def sumar(a,b):
    c = a + b
    print("Resultado es :"+c)

def restar(a,b):
    c= a - b
    print(c)

def menu():
    print("Seleccione una operacion \n 1-Sumar \n 2-restar \n 3-Multiplicacion :\n")
    s=input("Ingrese opcion: ")
    return s


def multiplicar(a,b):
    c= a*b
    print(c)
    

while True:
    opcion= menu()





    if opcion=='1' :
        sumar(x,y)
    
        menu()

    elif opcion=='2' :
        restar(x,y)
        menu()

    elif opcion=='3' :
        multiplicar(x,y)
        menu()
    else:
        print("Opcion no valida, intente de nuevo")




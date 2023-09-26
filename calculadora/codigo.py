#!C:/Users/zx22student3209/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\n")

x = int(input("Ingresa primer numero =\n"))
y = int(input("Ingresa segundo numero =\n"))
c=None


def sumar(a,b):
    c = a + b
    return print("Resultado es :",c)

def restar(a,b):
    c= a - b
    return print("Resultado es :",c)

def menu():
    print("Seleccione una operacion \n 1-Sumar \n 2-restar \n 3-Multiplicacion :\n 4-Salir\n")
    s=input("Ingrese opcion: ")
    return s


def multiplicar(a,b):
    c= a * b
    return print("Resultado es :",c)
    

while True:
    opcion= menu()






    if opcion=='1' :
        sumar(x,y)
    
        

    elif opcion=='2' :
        restar(x,y)
        

    elif opcion=='3' :
        multiplicar(x,y)

    elif opcion=='4':
        exit()
        
    else:
        print("Opcion no valida, intente de nuevo")




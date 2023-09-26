#!C:/Users/zx22student3209/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\n")

x = input("Ingresa primer numero")
y = input("Ingresa segundo numero")
c=0


def sumar():
    c = (x + y)
    print(c)

def dividir():
    c = x / y
    return c

print("Seleccione una operacion \n 1-Sumar \n 2-restar \n 3-Multiplicacion \n")

s=input()

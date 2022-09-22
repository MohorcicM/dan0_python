from decimal import Decimal


while True:
    op = str(input("Izberi operacijo, +, -, *, / : "))
    a = Decimal(input("Vnesi 1. st.:"))
    b = Decimal(input("Vnsei 2. st.:"))
    
    if op == '+':
        rezultat = a+b
        print("Rezultat = " + str(rezultat))
    elif op == '-':
        rezultat = a-b
        print("Rezultat = " + str(rezultat))
    elif op == '*':
        rezultat = a*b
        print("Rezultat = " + str(rezultat))
    elif op == '/':
        rezultat = a/b
        print("Rezultat = " + str(rezultat))
    else:
        print("Operacija ni veljavna")
    


    

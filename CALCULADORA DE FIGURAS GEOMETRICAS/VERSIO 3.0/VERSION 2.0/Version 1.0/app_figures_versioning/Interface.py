import math

def menu():
    print("1).Rectangulo\n2).Triangulo\n3).Cuadrado\n4).Circulo\n5).Pentagono\n6).Trapezio\n7).Romboide\n8).Rombo")
    option = ""

    try: 
        option = int(input("Selecciona: "))
        print()

        if option == 1:
            return 1
        
        elif option == 2:
            return 2
        
        elif option == 3:
            return 3
        
        elif option == 4:
            return 4
        
        elif option == 5:
            return 5
        
        elif option == 6:
            return 6
        
        elif option == 7:
            return 7
        
        elif option == 8:
            return 8
    
    except ValueError as value:
        print(f"Caracteres Permitidos: Solo números.")
        print()

def rectangleData():
    height = float(input("Ingresa Largo: "))
    weight = float(input("Ingresa Ancho: "))
    return height, weight

def triangleData():
    base = float(input("Ingresa Base: "))
    height = float(input("Ingresa Altura: "))
    return base, height

def squareData():
    side = float(input("Ingresa lado del Cuadrado: "))
    return side

def circleData():
    radio = float(input("Ingresa Radio: "))
    return radio

def pentagonData():
    perimeter = float(input("Ingresa Perimetro: "))
    apotema = float(input("Ingresa Apotema: "))
    return perimeter, apotema

def trapezeData():
    maxBase = float(input("Ingresa Base Mayor: "))
    minBase = float(input("Ingresa Base Menor: "))
    height = float(input("Ingresa Altura: "))
    return maxBase, minBase, height

def romboidwData():
    base = float(input("Ingresa Base: "))
    height = float(input("Ingresa Altura: "))
    return base, height

def diamondData():
    maxDiagonal = float(input("Ingresa Diagonal Mayor: "))
    minDiagonal = float(input("Ingresa Diagonal Menor: "))
    return maxDiagonal, minDiagonal
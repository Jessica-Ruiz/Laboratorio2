from Interface import *
from Figures import *
import os

os.system('cls')
print("Calculadora de figuras geométricas.")
flag = True
flagTwo =True

while flag: 

    option = menu()

    if option == 1:

        height, weight = rectangleData()
        print(f"Área de Rectangulo: {rectangleArea(height, weight)} centimetros cuadrados.")
        

    elif option == 2:

        base, height = triangleData()
        print(f"Área de Triangulo: {triangleArea(base, height)} centimetros cuadrados")

    elif option == 3:

        square = squareData()
        print(f"Área de Cuadrado: {squareArea(square)} centimetros cuadrados")

    elif option == 4:

        radius = circleData()
        print(f"Área del Circulo: {circleArea(radius)} centimetros cuadrados")

    elif option == 5:
        
        perimeter, apotema = pentagonData()
        print(f"Area del Pentagono: {pentagonArea(perimeter, apotema)} centimetros cuadrados")

    elif option == 6:

        maxBase, minBase, height = trapezeData()
        print(f"Area del Trapecio: {trapezeArea(maxBase, minBase, height)} centimetros cuadrados")

    elif option == 7:

        base, height = romboidwData()
        print(f"Área del Romboide: {romboidwArea(base, height)} centimetros cuadrados")

    elif option == 8:

        maxDiagonal, minDiagonal = diamondData()
        print(f"Área del Rombo: {diamondArea(maxDiagonal, minDiagonal)} centimetros cuadrados")

    while flagTwo:
        
        confirm = str(input("Continue? S | N: "))
        print()

        if confirm.upper() == "S":
            flagTwo = False

        elif confirm.upper() == "N":
            flagTwo = False
            flag = False
        
        else:
            print("Caracter Incorrecto!")
    
    flagTwo = True


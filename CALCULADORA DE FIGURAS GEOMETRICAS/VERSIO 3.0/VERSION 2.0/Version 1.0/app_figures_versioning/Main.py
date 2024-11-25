from Interface import *
from Figures import *
import os

os.system('cls')
print("Formulas de figuras geométricas.")
flag = True
flagTwo =True

while flag: 

    option = menu()

    if option == 1:

        height, weight = rectangleData()
        print(f"Área de Rectangulo: {rectangleArea(height, weight)} Metros Cuadrados.")

    elif option == 2:

        base, height = triangleData()
        print(f"Área de Triangulo: {triangleArea(base, height)}")

    elif option == 3:

        square = squareData()
        print(f"Área de Cuadrado: {squareArea(square)}")

    elif option == 4:

        radius = circleData()
        print(f"Área del Circulo: {circleArea(radius)}")

    elif option == 5:
        
        perimeter, apotema = pentagonData()
        print(f"Area del Pentagono: {pentagonArea(perimeter, apotema)}")

    elif option == 6:

        maxBase, minBase, height = trapezeData()
        print(f"Area del Trapecio: {trapezeArea(maxBase, minBase, height)}")

    elif option == 7:

        base, height = romboidwData()
        print(f"Área del Romboide: {romboidwArea(base, height)}")

    elif option == 8:

        maxDiagonal, minDiagonal = diamondData()
        print(f"Área del Rombo: {diamondArea(maxDiagonal, minDiagonal)}")

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
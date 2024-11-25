import random

matrixSensores = [] 

matrixTemps = []

row = 4

column = 4

print('Monitoreo de temperatura mediante sensores.\nMedición de valores de temperatura:\n\n - Bajos 0 > T < 10°\n\n - Medios >= 10° T < 25°\n\n - Altos 25° >= T < 55°\n\n - Criticos T >= 55°')


def createMatrixRandomValues(row, column):

    """Función encargada de generar una matriz n x m y
    llenar las posiciones con valores aleatorios."""

    for z in range(row):

        values = []

        for w in range(column):

            randValue = random.randint(0, 100)

            newValue = str(randValue) + " °C"

            values.append(newValue)

        matrixSensores.append(values)


createMatrixRandomValues(row, column)


def show(matrix):

    """Muestra la matriz"""

    for z in range(len(matrix)):
        print(end=f"\n\nF{z + 1}. ")

        print("")

        for w in range(len(matrix[0])): 

            if w % 2 == 0:
                print(end=f"| {matrix[z][w]} |")

            elif w == len(matrix[z]) - 1:
                print(end=f" {matrix[z][w]} |")

            elif w % 2 == 1:
                print(end=f" {matrix[z][w]} ")

        if z == len(matrix) - 1:
            print()


def search():

    """Permite buscar los valores bajo ciertas condiciones de temperatura."""

    chain = ""
    
    down = 0

    middle = 0

    high = 0

    critical = 0

    for z in range(len(matrixSensores)):

        for w in range(len(matrixSensores[0])):

            number = matrixSensores[z][w]

            for a in number:

                if a != '°' and a != 'C':

                    chain += a

            chain = int(chain)

            if chain >= 0 and chain < 10:

                down += 1

            elif chain >= 10 and chain < 25:

                middle += 1

            elif chain >= 25 and chain < 55:

                high += 1

            elif chain >= 55:

                critical += 1

            chain = ""
        
    matrixTemps.append(down)

    matrixTemps.append(middle)

    matrixTemps.append(high)

    matrixTemps.append(critical)

        
def printText():

    """Función encargada de mostrar los tipos de valores térmicos encontrados."""

    print(f"\n\nValores totales detectados: \n\n[ {matrixTemps[0]} ] -> valores Bajos.\n\n[ {matrixTemps[1]} ] -> Valores Medios.\n\n[ {matrixTemps[2]} ] -> Valores Altos.\n\n[ {matrixTemps[3]} ] -> Valores Criticos.")

show(matrixSensores)

search()

printText()
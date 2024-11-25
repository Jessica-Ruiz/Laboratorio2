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
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            height = float(input("Ingresa Largo: "))
            weight = float(input("Ingresa Ancho: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if height <= 0 or weight <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return height,weight
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return height,weight
def triangleData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            base = float(input("Ingresa Base: "))
            height = float(input("Ingresa Altura: "))

        #Anadi condicional que marque margen de error ante los valores negativos
            if base <= 0 or height <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return base, height
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return base,height

def squareData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")    
            side = float(input("Ingresa lado del Cuadrado: "))
            
        #Anadi condicional que marque margen de error ante los valores negativos
            if side <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return side
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return side

def circleData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            radio = float(input("Ingresa Radio: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if radio <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return radio
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return radio

def pentagonData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            perimeter = float(input("Ingresa Perimetro: "))
            apotema = float(input("Ingresa Apotema: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if perimeter <= 0 or apotema <=0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return perimeter, apotema
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return perimeter,apotema
def trapezeData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            maxBase = float(input("Ingresa Base Mayor: "))
            minBase = float(input("Ingresa Base Menor: "))
            height = float(input("Ingresa Altura: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if maxBase <= 0 or minBase <= 0 or height <=0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return maxBase, minBase, height
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return maxBase,minBase,height


def romboidwData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            base = float(input("Ingresa Base: "))
            height = float(input("Ingresa Altura: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if base <= 0 or height <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return base, height
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return base,height

def diamondData():
    """
    Esta es la funcion donde se solicitan los input de las medidas 
    correspondientes a la figura ademas se le agrego un bucle while 
    como verdadero con un try except para que cuando el usuario se 
    equivoque se reinicie el bucle y pueda continuar.

    """
    while True:
        try:
            notificacion=print(f"Si el valor numerico que va ingresar es decimal tenga en cuenta que en este aplicativo los valores decimales se escriben con punto y no con coma.De lo contrario haga caso omiso")
            maxDiagonal = float(input("Ingresa Diagonal Mayor: "))
            minDiagonal = float(input("Ingresa Diagonal Menor: "))
        #Anadi condicional que marque margen de error ante los valores negativos
            if maxDiagonal <= 0 or minDiagonal <= 0:
                print("No puede ingresar valores negativos por favor intente nuevamente con valores positivos.Gracias")
            else:
                return maxDiagonal, minDiagonal
        except ValueError:
            print(f"Intente nuevamente ingresando un valor numerico")
    return maxDiagonal,minDiagonal


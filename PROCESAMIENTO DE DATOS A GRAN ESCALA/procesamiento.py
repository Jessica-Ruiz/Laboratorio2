# Lista para almacenar el número de accesos por usuario
accesos_por_usuario = []

# Bucle del menu
while True:
    # Menú de opciones
    print("\nMenu:")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Salir")
    opcion = input("Seleccione una opción (1, 2, 3): ")
    
    if opcion == '1':
        # Solicitar nombre,hora de entrada,hora de salida
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")
        hora_salida = input("Ingrese la hora de salida (HH:MM): ")
        #for para buscar y contar los accesos por usuario
        encontrado = False
        for acceso in accesos_por_usuario:
            if acceso[0] == nombre_usuario:
                acceso[1] += 1  
                encontrado = True
                break
        
        # Si el usuario no está en la lista ingresa su usuario.
        if not encontrado:
            accesos_por_usuario.append([nombre_usuario, 1])
    
    elif opcion == '2':
# Mostrar los datos de accesos por usuario
        if not accesos_por_usuario:
            print("No hay datos registrados.")
        else:
            print("\nNúmero de accesos por usuario:")
            for usuario, accesos in accesos_por_usuario:
                print(f"{usuario}: {accesos}")
    
    elif opcion == '3':
    # Salir del programa
        print("Saliendo del programa...")
        break
    
    else:
    # Opcion invalida-
        print("Opción inválida, por favor ingrese una opción válida.")

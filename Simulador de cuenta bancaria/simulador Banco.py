import random 
from collections import deque 

class CuentaBancaria: 
    
    def __init__(self, titular, saldo_inicial=0): 
        self.titular = titular 
        self.saldo = saldo_inicial 

    def depositar(self, cantidad): 
        self.saldo += cantidad 
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}") 

    def retirar(self, cantidad): 
        if cantidad > self.saldo: 
            print("Fondos insuficientes.") 
        else: 
            self.saldo -= cantidad 
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}") 
    def consultar_saldo(self): 
        print(f"Saldo actual de {self.titular}: {self.saldo}") 
        
def seleccionar_cuenta(cuentas): 
    for usu, cuenta in enumerate(cuentas): 
        print(f"{usu + 1}. {cuenta.titular}") 
    
    while True: 
        try: 
            seleccion = int(input("Seleccione el número del usuario en la fila: ")) - 1  
            if 0 <= seleccion < len(cuentas): 
                return cuentas[seleccion] 
            else: 
                print("El usuario seleccionado no está en la fila.") 
        except ValueError: 
            print("Por favor, ingrese un número válido.") 

def menu(): 
    print("Qué operación desea realizar:") 
    print("1. Depósito") 
    print("2. Retiro") 
    print("3. Consulta de saldo") 
    while True: 
        try: 
            opcion = int(input("Seleccione la operación que desea realizar: ")) 
            if 1 <= opcion <= 3: 
                return opcion 
            else: print("Selección no válida.") 
        except ValueError: 
            print("Por favor, ingrese un número válido.") 
            
def procesar_clientes(Fila, cuentas): 
    print("1. Esteban") 
    print("2. Jessica") 
    print("3. Dinalut") 
    print("4. David") 
    while Fila: 
        usuario = Fila.popleft() 
        cuenta = cuentas[usuario] 
        
        while True: 
            print(f"Atendiendo al usuario: {cuenta.titular}") 
            opcion = menu() 
            if opcion == 1: 
                while True: 
                    try: 
                        cantidad = float(input("Ingrese la cantidad a depositar: ")) 
                        cuenta.depositar(cantidad) 
                        break 
                    except ValueError: 
                        print("Por favor, ingrese un número válido.") 

            elif opcion == 2: 
                while True: 
                    try: 
                        cantidad = float(input("Ingrese la cantidad a retirar: ")) 
                        cuenta.retirar(cantidad) 
                        break 
                    except ValueError: 
                        print("Por favor, ingrese un número válido.") 
            
            elif opcion == 3: 
                cuenta.consultar_saldo() 

            continuar = input("¿Desea realizar otra operación? (si/no): ").lower() 
            if continuar != 'si': 
                print("gracias por su transaccion")
                break 
            
Fila = deque([0, 1, 2, 3]) 
usuario = 0 

# Crear algunas cuentas bancarias que están en una fila 
print("Fila de clientes.") 
cuenta1 = CuentaBancaria("Esteban", 500) 
cuenta2 = CuentaBancaria("Jessica", 300) 
cuenta3 = CuentaBancaria("Dinalut", 1000) 
cuenta4 = CuentaBancaria("David", 5000) 

# Lista de la fila de clientes 
cola_de_clientes = [cuenta1, cuenta2, cuenta3, cuenta4] 
# Procesar la fila de clientes 
procesar_clientes(Fila, cola_de_clientes)
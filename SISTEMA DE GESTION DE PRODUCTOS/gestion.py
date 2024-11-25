from tabulate import tabulate

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        """Aumenta la cantidad en inventario."""
        self.cantidad += cantidad
        print(f"Se han añadido {cantidad} unidades de {self.nombre}. Nuevo stock: {self.cantidad}")

    def disminuir_stock(self, cantidad):
        """Disminuye la cantidad en inventario."""
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Nuevo stock: {self.cantidad}")
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad} unidades.")

    def mostrar_producto(self):
        """Muestra la información del producto."""
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}"

def mostrar_inventario(inventario):
    """Muestra el inventario completo de manera tabular."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        # Crear una lista de listas con la información de cada producto
        tabla = []
        for producto in inventario:
            tabla.append([producto.nombre, producto.precio, producto.cantidad])
        
        # Usar tabulate para formatear y mostrar la tabla
        print(tabulate(tabla, headers=["Nombre", "Precio", "Cantidad"], tablefmt="grid"))

def mostrar_menu():
    """Muestra el menú principal."""
    print("\nMenú:")
    print("1. Ver inventario")
    print("2. Comprar producto")
    print("3. Vender producto")
    print("4. Salir")

def comprar_producto(inventario):
    """Simula la compra de productos (aumento de stock)."""
    mostrar_inventario(inventario)
    try:
        nombre_producto = input("Introduce el nombre del producto a comprar: ").capitalize()
        cantidad = int(input(f"¿Cuántas unidades de {nombre_producto} deseas comprar?: "))
        if cantidad<0:
            print("Intente nuevemente con un valor positivo")
            return
        # Buscar el producto en el inventario
        producto_encontrado = False
        for producto in inventario:
            if producto.nombre.lower() == nombre_producto.lower():
                producto.aumentar_stock(cantidad)
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")
    
    except ValueError:
        print("Por favor, introduce un número válido para la cantidad.")

def vender_producto(inventario):
    """Simula la venta de productos (disminución de stock)."""
    # Muestra el inventario antes de la venta para que el usuario vea la cantidad actual
    mostrar_inventario(inventario)
    try:
        nombre_producto = input("Introduce el nombre del producto a vender: ").capitalize()
        cantidad = int(input(f"¿Cuántas unidades de {nombre_producto} deseas vender?: "))
        if cantidad<0:
            print("Intente nuevemente con un valor positivo")
            return
        # Buscar el producto en el inventario
        producto_encontrado = False
        for producto in inventario:
            if producto.nombre.lower() == nombre_producto.lower():
                producto.disminuir_stock(cantidad)
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")
    
    except ValueError:
        print("Por favor, introduce un número válido para la cantidad.")

    # Muestra el inventario después de la venta para que el usuario vea el stock actualizado
    mostrar_inventario(inventario)

# Crear una lista de productos (inventario)
producto1 = Producto("Cemento Argos Gris 50 kg", 30000, 50)
producto2 = Producto("Bloque N4 estandar x Unidad", 1350, 5000)
producto3 = Producto("Grava x metro", 132250, 1500)
producto4 = Producto("Arena x Metros", 80000, 2000)

# Almacenamos los productos en una lista (inventario)
inventario = [producto1, producto2, producto3, producto4]

# Menú interactivo
while True:
    mostrar_menu
    try:
        opcion = int(input("Elige una opción (1-4): "))
        
        if opcion == 1:
            print("\nInventario actual:")
            mostrar_inventario(inventario)
        elif opcion == 2:
            comprar_producto(inventario)
        elif opcion == 3:
            vender_producto(inventario)
        elif opcion == 4:
            print("¡Gracias por usar el sistema de gestión de inventarios!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


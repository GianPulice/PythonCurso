def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def agregar_producto(lista_productos):
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intente nuevamente: ").strip()

    categoria = input("Ingrese la categoría del producto: ").strip()
    while not categoria:
        categoria = input("La categoría no puede estar vacía. Intente nuevamente: ").strip()

    while True:
        precio = input("Ingrese el precio del producto (sin centavos): ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("El precio debe ser un número entero.")

    lista_productos.append([nombre, categoria, precio])
    print("Producto agregado")

def mostrar_productos(lista_productos):
    if not lista_productos:
        print("No hay productos registrados.")
        return

    print("\n--- Lista de Productos ---")
    for i, producto in enumerate(lista_productos, 1):
        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")

def buscar_producto(lista_productos):
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    resultados = [p for p in lista_productos if nombre_buscado in p[0].lower()]

    if resultados:
        print("\n--- Resultados de la búsqueda ---")
        for producto in resultados:
            print(f"Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
    else:
        print("No se encontraron productos con ese nombre.")

def eliminar_producto(lista_productos):
    if not lista_productos:
        print("No hay productos para eliminar.")
        return

    mostrar_productos(lista_productos)

    while True:
        try:
            pos = int(input("Ingrese el número del producto a eliminar: "))
            if 1 <= pos <= len(lista_productos):
                eliminado = lista_productos.pop(pos - 1)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                break
            else:
                print("Número inválido. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

productos = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_producto(productos)
    elif opcion == "2":
        mostrar_productos(productos)
    elif opcion == "3":
        buscar_producto(productos)
    elif opcion == "4":
        eliminar_producto(productos)
    elif opcion == "5":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor elija entre 1 y 5.")

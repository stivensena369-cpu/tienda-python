from productos import obtener_productos, mostrar_productos
from pedidos import agregar_pedido, mostrar_pedido
from historial import guardar_historial, ver_historial

productos = obtener_productos()
pedido_actual = []

while True:
    print("\n====== TIENDA ======")
    print("1. Ver productos")
    print("2. Agregar producto al pedido")
    print("3. Listar mi pedido")
    print("4. Ver historial de compras")
    print("5. Guardar compra")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_productos(productos)

    elif opcion == "2":
        mostrar_productos(productos)
        agregar_pedido(productos, pedido_actual)

    elif opcion == "3":
        mostrar_pedido(pedido_actual)

    elif opcion == "4":
        ver_historial()

    elif opcion == "5":
        guardar_historial(pedido_actual)
        print("Compra guardada correctamente")

    elif opcion == "6":
        print("Gracias por usar la tienda")
        break

    else:
        print("Opción inválida")
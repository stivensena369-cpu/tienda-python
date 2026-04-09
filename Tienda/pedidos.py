def agregar_pedido(productos, pedido_actual):
    opcion = int(input("Seleccione el número del producto: "))
    cantidad = int(input("Ingrese cantidad: "))

    producto = productos[opcion - 1]

    total = producto["precio"] * cantidad

    pedido_actual.append({
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio": producto["precio"],
        "total": total
    })

    print("Producto agregado al pedido")


def mostrar_pedido(pedido_actual):
    print("\n--- MI PEDIDO ---")
    total_general = 0

    for p in pedido_actual:
        print(f"{p['nombre']} | Cantidad: {p['cantidad']} | Precio: {p['precio']} | Total: {p['total']}")
        total_general += p["total"]

    print("TOTAL A PAGAR:", total_general)
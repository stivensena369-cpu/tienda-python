def obtener_productos():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]
    return productos


def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")
    for i, p in enumerate(productos, 1):
        print(f"{i}. {p['nombre']} - $ {p['precio']}")
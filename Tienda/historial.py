def guardar_historial(pedido_actual):
    with open("historial.txt", "a") as archivo:
        for p in pedido_actual:
            linea = f"{p['nombre']} | {p['cantidad']} | {p['precio']} | {p['total']}\n"
            archivo.write(linea)


def ver_historial():
    print("\n--- HISTORIAL DE COMPRAS ---")

    try:
        with open("historial.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("No hay historial aún")
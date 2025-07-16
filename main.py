inventario={}

cantidad=int(input("Ingrese la cantidad de productos: "))

for i in range(cantidad):
    print(f"\nProducto #{i+1}")

    while True:
        codigo=input("Ingrese el codigo del producto: ")
        if codigo in inventario:
            print("codigo ya existente")
        else:
            break

    nombre=input("Ingrese el nombre del producto: ")

    categoria=input("Ingrese(Hombre,mujer,niño)")

    while True:
        talla=input("Ingrese la tallea: ")
        if talla in ["S", "M", "L", "XL"]:
            break
        else:
            print("Talla no existente")

    while True:
        precio=float(input("Ingrese el precio del producto: "))

        if precio>0:
            break
        else:
            print("El precoo deve ser mayor a 0")

    while True:
        Enstok=int(input("Ingrese la cantidad en stok del producto: "))

        if Enstok>=0:
            break
        else:
            print("La cantidad bede ser positiva")

    inventario[codigo]={
        "nombre":nombre,
        "categoria":categoria,
        "precio":precio,
        "Enstok":Enstok,
        "Talla":talla,
    }

print("\nInventario registrado")
for codigo in inventario:
    print(f"\nProducto #{codigo}")
    print(f"Nombre: {inventario[codigo]['nombre']}")
    print(f"Categoria: {inventario[codigo]['categoria']}")
    print(f"Precio: {inventario[codigo]['precio']}")
    print(f"Enstok: {inventario[codigo]['Enstok']}")
    print(f"Talla: {inventario[codigo]['Talla']}")
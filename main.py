inventario={}

cantidad=int(input("\nIngrese la cantidad de productos: "))

for i in range(cantidad):
    print(f"\nProducto #{i+1}")

    while True:
        codigo=input("\nIngrese el codigo del producto: ")
        if codigo in inventario:
            print("codigo ya existente")
        else:
            break

    nombre=input("\nIngrese el nombre del producto: ")

    categoria=input("\nIngrese (Hombre,mujer,niño): ")

    while True:
        talla=input("\nIngrese la tallea (S,M,L,XL): ")
        if talla in ["S", "M", "L", "XL"]:
            break
        else:
            print("Talla no existente")

    while True:
        precio=float(input("\nIngrese el precio del producto: "))

        if precio>0:
            break
        else:
            print("El precoo deve ser mayor a 0")

    while True:
        Enstok=int(input("\nIngrese la cantidad en stock del producto: "))

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
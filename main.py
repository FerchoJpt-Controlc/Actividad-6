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



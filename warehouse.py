from jasd import main_app
import clases
status = None
main_app()
while status != 'exit':
    productos_existentes = []
    print("Gracias por usar la aplicación. Seleccione las siguientes opciones para habilitar inventario: ")
    choice = int(input("1. Agregar algo al inventario\n2. Salir\n"))
    if choice == 1:
        product_name = input("Ingrese el nombre del producto: ")
        product_code = input("Ingrese el código del producto: ")
        
        nombre_unico = f"{product_name}--{product_code}"
        if nombre_unico in productos_existentes:
            print("El producto ya existe en el inventario.")
            continue
        else:
            product_category = input("Ingrese la categoría del producto: ")
            product_type = input("Ingrese el tipo de producto: ")
            product_brand = input("Ingrese la marca del producto: ")
            product_supplier = input("Ingrese el proveedor del producto: ")
            product_description = input("Ingrese la descripción del producto: ")
            producto_new = clases.Producto(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
        productos_existentes.append(nombre_unico)

from .operations import *
from os import system

def execute_menu():
    while True:
        print("\033[33m" + "\nSistema de Control de Stock" + "\033[0m")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Registrar Compra")
        print("4. Registrar Venta")
        print("5. Listar Productos")
        print("6. Sin Stock")
        print("7. Actualizar Precio")
        print("8. Salir")
        opcion = input("\nElige una opción: ")


        # ADD
        if opcion == "1": 
            system("clear")
            name = input("Nombre del producto: ")
            category = input("Categoría: ")
            price = float(input("Precio: "))
            product_create(name, category, price)
            system("clear")
            print("Producto agregado con éxito.")
        
        # DELETE
        elif opcion == "2":
            id = int(input("ID del producto: "))
            product_delete(id)
            system("clear")
            print("Producto eliminado con éxito.")

        # BUY
        elif opcion == "3":
            id = int(input("ID del producto: "))
            amount = int(input("Cantidad: "))
            success = register_buy(id, amount)
            system("clear")
            
            if success == None:
                print("Producto Inexistente.")
            else:
                print("Compra registrada con éxito.")

        # SALE
        elif opcion == "4":
            id = int(input("ID del producto: "))
            amount= int(input("Cantidad: "))

            success = register_sale(id, amount)
            system("clear")

            if success == None:
                print("Venta sin éxito.")
            else:
                system("clear")
                print("Venta realizada con éxito.")

        # LIST PRODUCT
        elif opcion == "5":
            system("clear")
            products = product_list()
            for p in products:
                print(f"ID: {p.id}, Nombre: {p.name}, Categoría: {p.category}, Precio: {p.price}, Stock: {p.current_stock}")


            print("-----------------------------------------------------------------------")

        # LOW STOCK LIST
        elif opcion == "6":
            system("clear")
            products = list_low_stock()
            for p in products:
                print(f"ID: {p.id}, Nombre: {p.name}, Stock: {p.current_stock}")

            print("----------------------------------------------")

        # UPDATE PRICE
        elif opcion == "7":
            id = int(input("ID del producto: "))
            new_price = float(input("Nuevo precio: "))
            success = update_price_product(id,new_price)
            system("clear")
            if success == None:
                print("Producto inexistente.")
            else:
                print("Precio actualizado.")

        # EXIT
        elif opcion == "8":
            system("clear")
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

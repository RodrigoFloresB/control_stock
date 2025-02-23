from tkinter import *
from .operations import *

def execute_window():

    # Window
    window = Tk()
    window.title("CONTROL STOCK")
    window.geometry("750x330")
    window.configure(bg="#536d88")

    # Operations

    def actualizar_listbox():
        listbox.delete(0, END)
        list_product = product_list()
        for p in list_product:
            product_str = f"ID: {p.id} | {p.name} | {p.category} | ${p.price} | Stock: {p.current_stock}"
            listbox.insert(END, product_str)

    def buyButton():
        datos = text_in.get().strip()
        try:
            id_producto, cantidad_str = datos.split(",")  # Divide por coma
            cantidad = int(cantidad_str)
            register_buy(id_producto.strip(), cantidad)
            actualizar_listbox()
            text_in.delete(0, END)
        except ValueError:
            text_in.delete(0, END)
            text_in.insert(0, "ID,Cantidad")

    def saleButton():
        datos = text_in.get().strip()
        try:
            id_producto, cantidad_str = datos.split(",")
            cantidad = int(cantidad_str)
            register_sale(id_producto.strip(), cantidad)
            actualizar_listbox()
            text_in.delete(0, END)
        except ValueError:
            text_in.delete(0, END)
            text_in.insert(0, "ID,Cantidad")

    def newButton():
        datos = text_in.get().strip()
        try:
            name, category, price = datos.split(",")
            price = int(price)
            product_create(name, category, price)
            actualizar_listbox()
            text_in.delete(0, END)
        except ValueError:
            text_in.delete(0, END)
            text_in.insert(0, "Name,Category,Price")

    def delButton():
        datos = text_in.get().strip()
        try:
            id_product = datos
            id_product = int(id_product)
            product_delete(id_product)
            actualizar_listbox()
            text_in.delete(0, END)
        except ValueError:
            text_in.delete(0, END)
            text_in.insert(0, "ID")

    # Buttons


    buttonFrame = Frame(window, bg="#536d88")
    buttonFrame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    button_buy = Button(buttonFrame, text="Buy", width=10, height=2,
                        command= lambda: buyButton())
    
    button_sale = Button(buttonFrame, text="Sale", width=10, height=2,
                        command= lambda: saleButton())
    
    button_new = Button(buttonFrame, text="New", width=10, height=2,
                        command= lambda: newButton())

    button_del = Button(buttonFrame, text="Del", width=10, height=2,
                        command= lambda: delButton())


    button_buy.pack(pady=5, fill="x")
    button_sale.pack(pady=5, fill="x")
    button_new.pack(pady=5, fill="x")
    button_del.pack(pady=5, fill="x")

    # Input
    
    frameInput = Frame(window)
    frameInput.grid(row=4, column=0, rowspan=4, padx=20, pady=10)

    text_in = Entry(frameInput, font="Arial 14")
    text_in.grid(padx=5, pady=5)
    text_in.bind("<Return>")


    # Listbox

    list_product = product_list()

    listboxFrame = Frame(window)
    listboxFrame.grid(row=0, column=2, rowspan=4, padx=20, pady=10)

    scrollbar = Scrollbar(listboxFrame, orient=VERTICAL)

    listbox = Listbox(listboxFrame, yscrollcommand=scrollbar.set, width=50, height=14)
    scrollbar.config(command=listbox.yview)

    for p in list_product:
        product_str = f"ID: {p.id} | {p.name} | {p.category} | ${p.price} | Stock: {p.current_stock}"
        listbox.insert(END, product_str)

    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)


    window.mainloop()
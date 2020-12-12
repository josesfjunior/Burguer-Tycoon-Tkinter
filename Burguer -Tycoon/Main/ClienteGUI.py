from tkinter import *
from cardapio import cardapio_click
from Mostrar_pedido import listagem_de_pedidos_feitos



def cliente():

    def cardapio():
        cliente_gui.destroy()
        cardapio_click()

    def mostrar_pedidos():
        cliente_gui.destroy()
        listagem_de_pedidos_feitos()

    cliente_gui = Tk()

    pedir_lanche = Button(cliente_gui, text = "Pedir lanches",width = 10, height = 5,bg= "#FA8072", fg = "Black" ,
    command = cardapio, bd= 4)
    pedir_lanche.place(x = 10, y = 10)

    mostrar_lanche = Button(cliente_gui, text = "Mostrar lanches",width = 10, height = 5,bg= "#FA8072", fg = "Black" ,
    command = mostrar_pedidos, bd= 4)
    mostrar_lanche.place(x = 140, y = 10)









    cliente_gui["bg"] = "#FA8072"
    cliente_gui.title("Burgue Tycon")
    cliente_gui.geometry("550x300+100+100")
    cliente_gui.mainloop()



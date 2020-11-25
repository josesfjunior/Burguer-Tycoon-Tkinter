from tkinter import*
from Server_Conect import *
from tkinter import font



#Guia de pedidos prontos
def listagem_de_pedidos_feitos():
    janela_pedidos = Tk()
    Font_Listbox = font.Font(family = "Rockwell", size = 15)
    Font_Label = font.Font(family = "Rockwell", size = 13)

    def enviar_e_atualizar():
        
        querry = """UPDATE pedido 
        SET status = 'R'
        where pedidoid = '{}'"""
        recebe_id = pedido_id.get(ACTIVE)
        update_status(querry.format(recebe_id))
        janela_pedidos.destroy()
        listagem_de_pedidos_feitos()

    comando = """select * from pedido where status = 'P' order by pedidoid"""
    pedidos_prontos = select_com_retorno_geral(comando)
    print(pedidos_prontos)
    
    pedido_id = Listbox(janela_pedidos,activestyle = 'dotbox', height = 5, font = Font_Listbox, fg = "green")
    pedido_id.place(x=1, y = 50)
    nome_pedido = Listbox(janela_pedidos,activestyle = 'dotbox', height = 5, font = Font_Listbox, fg = "green")
    nome_pedido.place(x = 230, y =50)

    for pedido in pedidos_prontos:
        pedido_id.insert(END,pedido[0])
        nome_pedido.insert(END,pedido[1])


    enviar = Button(janela_pedidos,text = "Enviar", command = enviar_e_atualizar )
    enviar.place(x = 70, y = 250)
    sair = Button(janela_pedidos,text = "Sair", command = quit)
    sair.place(x = 5 ,y = 250)



    janela_pedidos.geometry("660x300")
    janela_pedidos.mainloop()


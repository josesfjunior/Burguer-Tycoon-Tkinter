from tkinter import *
from Server_Conect import *
from tkinter import font
    

# Função para exportação que contem a parte de fazer todos os pedidos
def funcionario():
    janela_funcionario = Tk()
    Font_Listbox = font.Font(family = "Rockwell", size = 12)
    Font_Label = font.Font(family = "Rockwell", size = 16)

    def enviar_e_atualizar():
        
        querry = """UPDATE pedido 
        SET status = 'P'
        where pedidoid = '{}'"""
        recebe_id = lista_id.get(ACTIVE)
        update_status(querry.format(recebe_id))
        janela_funcionario.destroy()
        funcionario()

    comando = """Select * from pedido
    where status = 'F'"""
    pedidos_para_fazer = select_com_retorno_geral(comando)
#listboxs para adcicornas as informaçoes a tela
    lista_id= Listbox(janela_funcionario,activestyle = 'dotbox', height = 5, font = Font_Listbox)
    lista_id.place(x = 1, y= 50)

    lista_cliente= Listbox(janela_funcionario,activestyle = 'dotbox', height = 5, font = Font_Listbox)
    lista_cliente.place(x = 190, y= 50)

    lista_lanche= Listbox(janela_funcionario,activestyle = 'dotbox', height = 5, font = Font_Listbox)
    lista_lanche.place(x = 380, y= 50)

    lista_quantidade= Listbox(janela_funcionario,activestyle = 'dotbox', height = 5, font = Font_Listbox)
    lista_quantidade.place(x = 570, y= 50)

    lista_status= Listbox(janela_funcionario,activestyle = 'dotbox', height = 5, font = Font_Listbox)
    lista_status.place(x = 760, y= 50)
#for de adição dos dados do servidor
    for row in pedidos_para_fazer:
        lista_id.insert(END,row[0])
        lista_cliente.insert(END,row[1])
        lista_lanche.insert(END,row[3])
        lista_quantidade.insert(END,row[2])
        lista_status.insert(END,row[4])

    butao_test = Button(janela_funcionario,text = "Enviar", command = enviar_e_atualizar )
    butao_test2 = Button(janela_funcionario,text = "Voltar")
    butao_test.place(x = 1, y = 250)

#labels de textos
    id_pedido = Label(janela_funcionario,text = "Numero do Pedido :", font = Font_Label, )

    
    janela_funcionario.title("Burgue Tycon")
    janela_funcionario.geometry("1000x300+100+100")
    janela_funcionario.mainloop()

funcionario()
from tkinter import *
from Server_Conect import *
from tkinter import font


# Função para exportação que contem a parte de fazer todos os pedidos
def funcionario():
    janela_funcionario = Tk()
    Font_Listbox = font.Font(family = "Rockwell", size = 12)
    Font_Label = font.Font(family = "Rockwell", size = 13)


    def enviar_e_atualizar():
        
        querry = """UPDATE pedido 
        SET status = 'P'
        where pedidoid = '{}'"""
        recebe_id = lista_id.get(ACTIVE)
        update_status(querry.format(recebe_id))
        janela_funcionario.destroy()
        funcionario()
        

    comando = """SELECT p.pedidoid, p.nome_cliente, p.quantidade, p.lancheid, l.lanche, p.status  FROM pedido p, lanche l
where p.lancheid = l.lancheid and p.status = 'F'"""
    pedidos_para_fazer = select_com_retorno_geral(comando)

    #comando_dois = """select lanche.lanche from lanche, pedido where pedido.lancheid = lanche.lancheid """
    #outro_seclect  = select_com_retorno_geral(comando_dois)
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
        lista_lanche.insert(END,row[4])
        lista_quantidade.insert(END,row[2])
        lista_status.insert(END,row[5])


    enviar = Button(janela_funcionario,text = "Enviar", command = enviar_e_atualizar )
    enviar.place(x = 70, y = 250)
    sair = Button(janela_funcionario,text = "Sair", command = quit)
    sair.place(x = 5 ,y = 250)

    #labels de textos
    id_pedido = Label(janela_funcionario,text = "Numero do Pedido:", font = Font_Label, fg = "#FA8072" )
    id_pedido.place(x = 2, y = 20)
    nome_cliente = Label(janela_funcionario,text = "Nome do Cliente:", font = Font_Label, fg = "#FA8072")
    nome_cliente.place(x = 193, y = 20)
    lanche_id = Label(janela_funcionario,text = "Lanche:", font = Font_Label, fg = "#FA8072")
    lanche_id.place(x = 440, y = 20)
    quantidade_nome= Label(janela_funcionario,text = "Quantidade:", font = Font_Label, fg = "#FA8072")
    quantidade_nome.place(x= 600, y = 20)
    status_nome = Label(janela_funcionario,text = "Status:", font = Font_Label, fg = "#FA8072")
    status_nome.place(x = 830, y =20)
    
    
    
    janela_funcionario.title("Burgue Tycon")
    janela_funcionario.geometry("1000x300+100+100")
    janela_funcionario.mainloop()


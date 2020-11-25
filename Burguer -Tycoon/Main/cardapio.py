from Server_Conect import *
from tkinter import* 
from psycopg2 import *
from verficar_id import verificar_id

def cardapio_click():
    
    comando = """select * from lanche"""
    slect_servidor = select_com_retorno_geral(comando)
    retorno_lanche_servidor = []
    retorno_preco_servidor = []

    def resposta_click():
            resposta_lanche = lista_lanche.get(ACTIVE)
            resposta_escolha = quantidade_escolha.get()
            resposta_nome = recebe_nome.get()
            num = verificar_id(resposta_lanche)
            insercao_bd = """INSERT INTO pedido(nome_cliente,quantidade,lancheid,status)
            VALUES ('{}','{}','{}','F')"""
            conexao_de_insert(insercao_bd.format(resposta_nome,resposta_escolha,num))

    for row in slect_servidor: 
        retorno_lanche_servidor.append(row[1])
        retorno_preco_servidor.append(row[2])

    menu_cardapio = Tk()

    lista_lanche = Listbox(menu_cardapio, height = 10,  width = 30,  bg = "#FA8072", activestyle = 'dotbox',  font = "Rockwell", fg = "yellow", bd = 4)
    lista_lanche.place(x= 10, y= 30)
    lista_lanche.insert(END)
    for lanches in retorno_lanche_servidor:
        lista_lanche.insert(END, lanches)

    lista_preco = Listbox(menu_cardapio, height = 10,  width = 10,  bg = "#FA8072", activestyle = 'dotbox',  font = "Rockwell", fg = "yellow", bd = 4)
    lista_preco.place(x = 300, y =30)
    lista_preco.insert(END)
    for precos in retorno_preco_servidor:
        lista_preco.insert(END,precos)


    cardapio = Label(menu_cardapio, text = " Menu ", bg = "#FA8072")
    cardapio.place(x = 130 ,y = 8) 

    preco = Label(menu_cardapio, text = " Preço ", bg = "#FA8072")
    preco.place(x = 320 , y =8)

    sair = Button(menu_cardapio, width = 5 , text = "Sair", bg= "#FA8072", fg = "Black",command = quit)
    sair.place(x = 10, y =260)

    enviar = Button(menu_cardapio, width = 5 , text = "Enviar", bg= "#FA8072", fg = "Black",command = resposta_click)
    enviar.place(x = 100, y = 260)

    quantidade_escolha = Spinbox(menu_cardapio, from_=1, to = 10)
    quantidade_escolha.place(x =440, y =170)

    quantidade_nome = Label(menu_cardapio, text = "Quantidade :", bg = "#FA8072")
    quantidade_nome.place(x = 490, y = 140)

    nome_cliente = Label(menu_cardapio,text = "Nome do Cliente :" , bg = "#FA8072" )
    nome_cliente.place(x= 465, y =50)

    recebe_nome = Entry(menu_cardapio)
    recebe_nome.place(x= 450, y = 80)

    menu_cardapio["bg"] = "#FA8072"
    menu_cardapio.title("Burgue Tycon")
    menu_cardapio.geometry("660x300+100+100")
    menu_cardapio.mainloop()


from tkinter import *
from Server_Conect import *


def cadastrar():

    janela_cadastro = Tk()

    def completar():
        recebe_nome = cadastro.get()
        comando = """Insert into funcionario(nome_funcionario)
        values('{}')"""
        conexao_de_insert(comando.format(recebe_nome))
        cadastrado = Label(janela_cadastro, text = 'Cadastrado', bg = "#FA8072" )
        cadastrado.place(x = 250, y = 30)
        
    #entry

    cadastro = Entry(janela_cadastro)
    cadastro.place(x = 70, y = 30)

    #label

    nome = Label(janela_cadastro, text = "Nome : ", bg = "#FA8072")
    nome.place(x = 1, y =30)

    #botão

    enviar = Button(janela_cadastro, text ="Enviar", command = completar)
    enviar.place(x = 100, y = 100)


    janela_cadastro["bg"] = "#FA8072"
    janela_cadastro.geometry("660x300+440+120")
    janela_cadastro.mainloop()



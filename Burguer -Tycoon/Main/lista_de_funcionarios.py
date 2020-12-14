from tkinter import *
from tkinter import font
from Server_Conect import *

def listagem_de_funcionarios():
    
    def demitir():
        demitido = id_funcionario.get(ACTIVE)
        demitir_comando = """Delete from funcionario where funcionarioid = '{}'"""
        apagar = update_status(demitir_comando.format(demitido))
        janela_main.destroy()
        listagem_de_funcionarios()

    janela_main = Tk()

    comando = """select * from funcionario"""
    retorno_sevidor = select_com_retorno_geral(comando)

    #Listboxs

    id_funcionario = Listbox(janela_main,activestyle = 'dotbox', height = 5)
    id_funcionario.place(x= 1, y = 50)
    nome_funcionario = Listbox(janela_main,activestyle = 'dotbox', height = 5)
    nome_funcionario.place(x = 170, y =50)



    for row in retorno_sevidor:
        id_funcionario.insert(END,row[0])
        nome_funcionario.insert(END,row[1])

    #Labels

    id_nome = Label(janela_main,text = "Codigo Funcionario:", bg = "#FA8072")
    id_nome.place(x = 10, y = 10)
    funcionario_nome = Label(janela_main,text = "Nome do Funcionario:", bg = "#FA8072")
    funcionario_nome.place(x = 180, y = 10)

    #Botões

    demitir_botao = Button(janela_main, text = "Demitir", command = demitir)
    demitir_botao.place(x = 80, y =250)
    sair_botao = Button(janela_main,text = "Sair", command = quit)
    sair_botao.place(x = 5 ,y = 250)

    janela_main["bg"] = "#FA8072"
    janela_main.geometry("660x300+440+120")
    janela_main.mainloop()


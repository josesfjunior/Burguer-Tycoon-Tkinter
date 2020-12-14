from tkinter import *
from lista_de_funcionarios import listagem_de_funcionarios
from cadastro_funcionario import cadastrar


def pagina_funcionario_principal():
    janela_funcionario = Tk()

    def abrir_listagem():
        janela_funcionario.destroy()
        listagem_de_funcionarios()

    def abrir_cadastro():
        janela_funcionario.destroy()
        cadastrar()

    #botões

    cadastrar_funcionario = Button(janela_funcionario, width = 15 , height =5, text = "Pagina de Cadastro", bg= "#FA8072", fg = "Black" ,bd= 4, command = abrir_cadastro)
    cadastrar_funcionario.place(x = 1, y = 30)

    listagem_e_demissão_funcionario = Button(janela_funcionario, width = 15 , height =5, text = "Pagina de Listagem", bg= "#FA8072", fg = "Black" ,
    command = abrir_listagem, bd= 4)
    listagem_e_demissão_funcionario.place(x = 200, y = 30)



    janela_funcionario["bg"] = "#FA8072"
    janela_funcionario.geometry("660x300+440+120")
    janela_funcionario.mainloop()


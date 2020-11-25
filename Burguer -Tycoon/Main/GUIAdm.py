from tkinter import *
from tkinter import font
from cardapio import cardapio_click

#Janela de Autenticação do Adm
def Adm_GUI():
        janela = Tk()
        

        def produtos_lista():
                janela.destroy()
                cardapio_click()
                



        Font_Cabecario = font.Font(family = 'Rockwell', size = 30)
        Font_Caixas = font.Font(family = 'Rockwell', size = 10)
        Font_Buttons = font.Font(family = "Rockwell", size = 12)


        Burguer_Text = Label(janela, text = "BURGUER TYCOON", font = Font_Cabecario, bg= "#FA8072", fg = "#FFFF00")
        Burguer_Text.place(x = 90, y = 10)        

        cadastrar_produto = Button(janela,width = 15,height = 5,text = "Cadastrar Produtos",bg= "#FA8072",fg = "Black",bd = 4)

        listar_produtos = Button(janela,width = 15,height = 5,text = "Listar Produtos",bg= "#FA8072",fg = "Black",bd = 4, command = produtos_lista)
        listar_produtos.place(x = 180, y = 100)


        voltar = Button(janela, width = 5 , text = "Sair", bg= "#FA8072", fg = "Black",command = quit)
        voltar.place(x = 10, y =260)


        janela["bg"] = "#FA8072"
        janela.title("Burgue Tycon")
        janela.geometry("500x300+100+100")
        janela.mainloop()
        



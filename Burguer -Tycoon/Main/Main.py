
#https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841

from tkinter import *
from tkinter import font
from GUIAdm import Adm_GUI
from ClienteGUI import cliente
from Server_Conect import *
from funcionarioGUI import funcionario

def main():
    def Button_Click():
        Janela_Principal.destroy()
        Adm_GUI()

    def abrir_gui_cliente():
        Janela_Principal.destroy()
        cliente()
    def abrir_janela_funcionario():
        Janela_Principal.destroy()
        funcionario()

    Janela_Principal = Tk()


    Font_Cabecario = font.Font(family = 'Rockwell', size = 30)
    Font_Caixas = font.Font(family = 'Rockwell', size = 10)
    Font_Buttons = font.Font(family = "Rockwell", size = 12)


    Burguer_Text = Label(Janela_Principal, text = "BURGUER TYCOON", font = Font_Cabecario, bg= "#FA8072", fg = "#FFFF00")
    Burguer_Text.place(x = 90, y = 10)


    Adm_Button = Button(width = 10 , height =5, text = "Pagina Adm", font = Font_Buttons, bg= "#FA8072", fg = "Black" ,
    command = Button_Click, bd= 4)
    Adm_Button.place(x = 10, y = 100)
    

    cliente_button= Button(width = 10 , height =5, text = "Pagina Cliente", font = Font_Buttons, bg= "#FA8072", fg = "Black" ,
    command = abrir_gui_cliente, bd= 4)
    cliente_button.place(x = 150, y = 100)

    funcionario_button= Button(width = 14 , height =5, text = "Pagina Funcionario", font = Font_Buttons, bg= "#FA8072", fg = "Black" ,
    command = abrir_janela_funcionario, bd= 3)
    funcionario_button.place(x = 300, y = 100)


    Janela_Principal["bg"] = "#FA8072"
    Janela_Principal.title("Burguer Tycoon")
    Janela_Principal.geometry("660x300+100+100")
    Janela_Principal.mainloop()

main()
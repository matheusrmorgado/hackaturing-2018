from tkinter import *

janela = Tk()

def bt_click():
    x = [int(ed1.get()),int(ed2.get()),(ed3.get())]
    if x[2] == "Sim":
        x[2] = 1
    else:
        x[2] = 0
    if x[1] <= 0.5:
        if x[2] <= 0.5:
            if x[0] <=0.5:
                resp = 99,2
            else:
                resp = 50
        else:
            resp = 97
    else:
        resp = 98
    
        
    resposta["font"] = ("Verdana", "14", "bold")
    resposta["text"] = 'Esta consulta tem '+ str(resp) + '%' + ' de chances de ser paga!'
    
    
janela.geometry("600x400+200+100")

lb = Label(janela, text="Entre com as informações da consulta")
lb.place(x=40, y=50)

lb1 = Label(janela, text="Serviço:")
lb1.place(x=40, y=115)

ed1 = Entry(janela)
ed1.place(x=200, y=115)

lb2 = Label(janela, text="Quantidade do Item:")
lb2.place(x=40, y=145)

ed2 = Entry(janela)
ed2.place(x=200, y=145)

lb3 = Label(janela, text="Tipo da guia é internação?")
lb3.place(x=40, y=175)

ed3 = Entry(janela)
ed3.place(x=200, y=175)

lb4 = Label(janela, text="É um medicamento?")
lb4.place(x=40, y=205)

ed4 = Entry(janela)
ed4.place(x=200, y=205)

lb5 = Label(janela, text="É urgente?")
lb5.place(x=40, y=235)

ed5 = Entry(janela)
ed5.place(x=200, y=235)

ok = Button(janela, width = 20, text="Submeter", command=bt_click)
ok.place(x=140, y=260)

resposta = Label(janela)
resposta.place(x=40, y=310)



janela.mainloop()
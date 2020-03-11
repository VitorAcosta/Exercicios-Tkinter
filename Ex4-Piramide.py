import tkinter as tk


class Tela:
    def __init__(self, master):
        #Associação da janela TopLevel(master) a um objeto (self.nossaTela)
        self.nossaTela = master

        self.fr1 = tk.Frame(self.nossaTela)
        self.fr1.pack()
        self.fr2 = tk.Frame(self.nossaTela)
        self.fr2.pack()
        self.fr3 = tk.Frame(self.nossaTela)
        self.fr3.pack()
        
        self.btn1 = tk.Button(self.fr1, text="1", width=3, height=2)
        self.btn1.pack()
        self.btn2 = tk.Button(self.fr2, text="2", width=3, height=2)
        self.btn2.pack(side = tk.LEFT)
        self.btn3 = tk.Button(self.fr2, text="3", width=3, height=2)
        self.btn3.pack(side = tk.LEFT)
        self.btn4 = tk.Button(self.fr3, text="4", width=3, height=2)
        self.btn4.pack(side = tk.LEFT)
        self.btn5 = tk.Button(self.fr3, text="5", width=3, height=2)
        self.btn5.pack(side = tk.LEFT)
        self.btn6 = tk.Button(self.fr3, text="6", width=3, height=2)
        self.btn6.pack(side = tk.LEFT)

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

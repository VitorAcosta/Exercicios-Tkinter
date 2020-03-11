import tkinter as tk


class Tela:
    def __init__(self, master):
        #Associação da janela TopLevel(master) a um objeto (self.nossaTela)
        self.nossaTela = master
        
        #Criação do primeiro label e posicionamento no topo.
        #(Lembre-se: por padrão o argumento side=tk.TOP sendo desnecessário a declaração)
        self.l1 = tk.Label(self.nossaTela, text="label 1",font=('Arial',16))
        self.l1.pack()
        
        #Criando o segundo label e posionando-o embaixo, definindo side=tk.BOTTOM
        self.l2 = tk.Label(self.nossaTela, text="label 2",font=('Arial',16))
        self.l2.pack(side=tk.BOTTOM)
        
        #Criando o terceiro label e posionando-o à esquerda, definindo side=tk.LEFT
        self.l3 = tk.Label(self.nossaTela, text="label 3",font=('Arial',16))
        self.l3.pack(side=tk.LEFT)

        #Criando o quarto label e posionando-o à direita, definindo side=tk.RIGHT
        self.l4 = tk.Label(self.nossaTela, text="label 4",font=('Arial',16))
        self.l4.pack(side=tk.RIGHT)

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

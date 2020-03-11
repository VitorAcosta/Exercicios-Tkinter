import tkinter as tk


class Tela:
    def __init__(self, master):
        #Criação de um objeto para a janela TopLevel.
        self.nossaTela = master

        #Criação da entrada de dados
        self.entrada1 = tk.Entry(self.nossaTela)
        self.entrada1.pack()
        
        #Criação da entrada de dados
        self.entrada2 = tk.Entry(self.nossaTela)
        self.entrada2.pack()
        
        #Criação do label com aspecto de botão, adicionando para estilização
        #o argumento relief="raised"
        self.labelClique = tk.Label(self.nossaTela, text="Somar", relief="raised")
        self.labelClique.pack()

        #Conexão entre o clique com o botão esquerdo do mouse com o método somar
        self.labelClique.bind('<Button-1>',self.somar)

    #Criação do método somar
    def somar(self, event):
        #Definição de duas variaveis que irão receber o objeto de Entry com o
        #método get(), retornando cada uma um valor em string, que será convertido
        #para inteiro através do 'int'.
        self.inteiro1 = int(self.entrada1.get())
        self.inteiro2 = int(self.entrada2.get())

        #Escreve no console a soma dos dois inteiros.
        print(self.inteiro1 + self.inteiro2)

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

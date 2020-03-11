import tkinter as tk


class Tela:
    def __init__(self, master):

        self.nossaTela = master

        self.texto1 = tk.Label(self.nossaTela, text="Insira seu nome:")
        self.texto1.pack(side=tk.LEFT)

        self.entrada = tk.Entry(self.nossaTela)
        self.entrada.pack(side=tk.LEFT)

        self.btn = tk.Button(self.nossaTela, text="Confirmar",bg='green', command=self.mostraNome)
        self.btn.pack(side=tk.LEFT, padx=10)

    def mostraNome(self):
        self.nome = self.entrada.get()
        print('Olá:' + self.nome)

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

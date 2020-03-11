import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext


class Tela:
    def __init__(self, master):
        self.nossaTela = master 

        #Configuração do menu da interface
        self.barraMenu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu = self.barraMenu)
        #Configuração do item do menu que abre a funcionalidade de ler o arquivo.
        self.barraMenu.add_command(label = "Ler arquivo", command=self.lerArquivo)

        self.areaTexto = scrolledtext.ScrolledText(self.nossaTela)
        self.areaTexto.pack(expand=True, fill=tk.BOTH)

    def lerArquivo(self):
        #Cria-se um diálogo que já retorna o objeto do tipo arquivo.
        caminho = filedialog.askopenfile(mode="r", initialdir = "/Downloads",
                                              title="Selecione um arquivo",
                                              filetypes = (("Arquivos de texto","*.txt"),("Arquivos Python","*.py")))
        #Se o usuário de fato escolheu um arquivo para ser aberto.
        if caminho:
            #O conteúdo é lido de toda a extensão do arquivo
            conteudo = caminho.read()
            self.areaTexto.insert(tk.INSERT,conteudo)
            
        else:
            print("Por favor escolha um arquivo")


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
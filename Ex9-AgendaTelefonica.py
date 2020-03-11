import tkinter as tk
from tkinter import filedialog


class Tela:
    def __init__(self, master):

        self.nossaTela = master

        #variavel de controle que verifica se já foi escolhido um arquivo
        #para o salvamento de dados. Evitando a abertura do FileDialog toda
        #vez que for necessário salvar um novo contato.
        self.arquivoAberto = None

        self.criaWidgets()

    #Método que cria e posiciona todos os widgets da interface
    def criaWidgets(self):

        self.lbl1 = tk.Label(self.nossaTela, text="Entre o nome:", font=('Arial',12))
        self.entradaNome = tk.Entry(self.nossaTela,font=('Arial',12))

        self.lbl2 = tk.Label(self.nossaTela, text="Entre com o telefone:", font=('Arial',12))
        self.entradaTel = tk.Entry(self.nossaTela,font=('Arial',12))

        self.cadastra = tk.Button(self.nossaTela, text="Cadastrar", command=self.salvar)

        self.lbl1.grid(column = 0)
        self.entradaNome.grid(row = 0,column = 1, padx=20)
        self.lbl2.grid(row=1,column=0)
        self.entradaTel.grid(row = 1,column = 1, padx=20)
        self.cadastra.grid(row = 2,column=0,columnspan=2,pady=20)


    def salvar(self):
        #Recuperando os dados das entradas de dados
        nome = self.entradaNome.get()
        telefone = self.entradaTel.get()

        #Se nenhum arquivo ainda foi definido como sendo o arquivo para o salvamento de dados
        if self.arquivoAberto is None:
            #É aberto o diálogo para a escolha do arquivo.
            #note que foi utilizado o asksaveasfilename, pois esse tipo de diálogo nos
            #retorna o caminho até o novo arquivo criado, possibilitando utilizar a variavel
            #de controle self.arquivoAberto.
            self.arquivoAberto = filedialog.asksaveasfilename(defaultextension = ".txt",
                                                filetypes = (("Arquivos de Texto","*.txt"),("Todos arquivos","*.*") ))

        #Se existe um caminho até o arquivo de salvamento
        if self.arquivoAberto is not None:
            #Abre o caminho em modo de append.
            dados = open(self.arquivoAberto,"a")

            #Escreve os dados inseridos na interface no arquivo criado pelo usuário.
            dados.write('\nNome:{}\n--->Telefone:{}'.format(nome,telefone))

            #Fecha o arquivo.
            dados.close()
        else:
            print("Erro")

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

import tkinter as tk


class Tela:
    def __init__(self,master):

        self.nossaTela = master

        self.frame = tk.Frame(self.nossaTela)
        self.frame.pack(ipadx=30,ipady=30)

        self.lbl = tk.Label(self.frame,text='Insira os segundos:')
        self.lbl.pack(side=tk.LEFT)

        self.entrada = tk.Entry(self.frame)
        self.entrada.pack(side=tk.LEFT, padx=20)

        self.btn = tk.Button(self.nossaTela,text="Converter", bg='red', command=self.conversor)
        self.btn.pack()

        self.saida = tk.Label(self.nossaTela, font=('Arial',16))
        self.saida.pack(pady=15)

    def conversor(self):
        segundos = int(self.entrada.get())
        hrs = str(segundos//3600) #O operador // realiza a divisão com arredondamento dos segundos inseridos com 3600
                              #que é a quantidade de segundos existentes em uma hora. Definindo a quantidade de horas
                              #existentes baseado na quantidade de segundos inseridos.
        
        mnt = str((segundos%3600)//60) #O operador % realiza o módulo (realiza a divisão e nos retorna o resto) 
                                   #entre os segundos inseridos e a quantidade de segundos em uma hora.
                                   #Após isso é realizado a divisão com arredondamento por 60 
                                   #(que é a quantidade de segundos em um minuto).

        seg = str((segundos%3600)%60) #É realizado o módulo dos segundos inseridos com 3600, e logo em seguida com
                                  #60, dessa forma, conseguimos definir a quantidade de segundos.

        conversao = "{} Horas {} Minutos {} Segundos".format(hrs, mnt, seg)
        self.saida['text'] = conversao



janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

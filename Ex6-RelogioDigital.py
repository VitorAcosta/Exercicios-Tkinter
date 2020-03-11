import tkinter as tk

#A biblioteca datetime permite a manipulação de datas e horários, e é integrada ao python por padrão.
import datetime

class Tela:
    def __init__(self, master):
        self.nossaTela = master        
        self.lblRelogio = tk.Label(self.nossaTela, font=('Arial',18), fg='blue')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        #A variavel agora receberá todos os dados referente ao relógio do sistema, isso é
        #o dia, mês e ano, além da hora, minuto, segundo e milissegundo.
        agora = datetime.datetime.now()

        #Como queremos exibir somente a hora, minuto e segundo em nosso relógio, utilizamos o método strftime,
        #que formata todas essas informações para o modo de exibição que queremos.
        #no site: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        #pode ser visualizado todos os códigos de formatação.
        self.lblRelogio['text'] = agora.strftime('%H:%M:%S')

        #O método after, após um delay (dado em milissegundos, logo 1000 ms = 1 s) invoca uma função,
        #que no caso, será a função que atualiza o texto do label.
        #Como o after chama a função, dentro da fução, todo o processo de alteração de horas, minutos e segundos ficará
        #em um loop.
        self.nossaTela.after(1000,self.alteracao)

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

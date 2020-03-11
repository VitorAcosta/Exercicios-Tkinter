import tkinter as tk


class Tela:

    def __init__(self, master):

        self.nossaTela = master

        #IntVar, StringVar ou BooleanVar

        self.cnt = tk.StringVar()

        self.rb1 = tk.Radiobutton(self.nossaTela, text="Python",
                                  variable = self.cnt, value = "Python")
        self.rb1.pack()
        self.rb1.select()

        self.rb2 = tk.Radiobutton(self.nossaTela, text="Java",
                                  variable = self.cnt, value = "Java")
        self.rb2.pack()
        
        self.rb3 = tk.Radiobutton(self.nossaTela, text="C++",
                                  variable = self.cnt, value = "C++")
        self.rb3.pack()

        self.btn = tk.Button(self.nossaTela, text="Confirmar", command = self.func)
        self.btn.pack()

        self.saida = tk.Label(self.nossaTela)
        self.saida.pack()

    def func(self):
        escolha = self.cnt.get()
        if(escolha == "Python"):
            self.saida['text'] = "print('Hello world')"
        elif(escolha == "Java"):
            self.saida['text'] = "System.out.println('Hello world')"
        else:
            self.saida['text'] = "std::cout << 'Hello world' << std::endl"


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()

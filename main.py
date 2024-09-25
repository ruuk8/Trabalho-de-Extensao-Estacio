import random
import string
from tkinter import *
from tkinter.ttk import *


class Aplication:
    resposta = ""
    def __init__(self, master = None):
        self.fonte = ("Arial", "20")
        self.container1 = Frame(master)
        self.container1.pack()
        self.container2 = Frame(master)
        
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7.pack()
                    
        self.titulo = Label(self.container1, text = "Gerador de Senhas")
        self.titulo["font"] = ("calibri", "20", "bold")
        self.titulo.pack()

        self.estado_1 = BooleanVar()
        self.estado_1.set(True)
        self.botao1 = Checkbutton(self.container1, text = "Incluir números", var = self.estado_1, onvalue = 1, offvalue = 0)
        self.botao1.pack(side = LEFT)

        self.estado_2 = BooleanVar()
        self.estado_2.set(True)
        self.botao2 = Checkbutton(self.container2, text = "Incluir letras maiúsculas", var = self.estado_2, onvalue = 1, offvalue = 0)
        self.botao2.pack(side = LEFT)

        self.estado_3 = BooleanVar()
        self.estado_3.set(True)
        self.botao3 = Checkbutton(self.container3, text = "Incluir letras minúsculas", var = self.estado_3, onvalue = 1, offvalue = 0)
        self.botao3.pack(side = LEFT)

        self.estado_4 = BooleanVar()
        self.estado_4.set(True)
        self.botao4 = Checkbutton(self.container4, text = "Incluir caracteres especiais", var = self.estado_4, onvalue = 1, offvalue = 0)
        self.botao4.pack(side = LEFT)

        self.botao5 = Label(self.container5, text = "Número de digitos na senha:")
        self.botao5.pack(side = LEFT)

        self.entrada = Entry(self.container5)
        self.entrada.pack(side = LEFT)

        self.mensagem = Label(self.container6, text = "")
        self.mensagem["font"] = ("Verdana", "10", "italic")
        self.mensagem.pack()
      
        self.botaoCopiar = Button(self.container6)
        self.botaoCopiar["text"] = "Copiar Senha"
        self.botaoCopiar["command"] = self.copiar_senha
        self.botaoCopiar.pack(side = LEFT)

        self.botaoGerar = Button(self.container7)
        self.botaoGerar["text"] = "Gerar Senha"
        self.botaoGerar.pack(side = LEFT)
        self.botaoGerar["command"] = self.respostaprograma

        self.botaoSair = Button(self.container7)
        self.botaoSair["text"] = "Sair"
        self.botaoSair.pack(side = LEFT)
        self.botaoSair["command"] = self.container7.quit
    
    #Declaração da função para copiar a senha no botão#
    def copiar_senha(self):
        self.container6 = Tk()
        self.container6.withdraw()
        self.container6.clipboard_clear()
        self.container6.clipboard_append(self.resposta)
        self.container6.update()
        self.botaoCopiar.place_forget()
    
    #Declaração da função para gerar senha#
    def gerador_senha(self, tamanho_senha = 8):
        
        #variáveis#
        senha = ""
        senha_usuario = ""

        #lista de opções#
        if self.estado_1.get() == True:
            senha += string.digits
        if self.estado_2.get() == True:
            senha += string.ascii_uppercase
        if self.estado_3.get() == True:
            senha += string.ascii_lowercase
        if self.estado_4.get() == True:
            senha += string.punctuation
        if senha == "":
            self.mensagem["text"] = "Escolha uma opção válida!"

        #loop para gerar senha#
        for i in range(0, tamanho_senha):
            digito_escolhido = random.choice(senha)
            senha_usuario = senha_usuario + digito_escolhido
        return senha_usuario

    def respostaprograma(self):
        

        #Verificação da entrada do usuário#
        escolha_usuario = self.entrada.get()

        if escolha_usuario.isdigit():
            escolha_usuario = int(escolha_usuario)
        else:
            self.mensagem["text"] = "Digite um número válido!"

        #Resposta do programa#
        self.resposta = self.gerador_senha(tamanho_senha = escolha_usuario)
        print(f"Senha gerada:\n{self.resposta}")
        self.mensagem["text"] = f"Senha gerada com sucesso!\n Senha: {self.resposta}"
       
 

janela = Tk()
Aplication(janela)
janela.mainloop()
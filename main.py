import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class TelaLogin():
    def __init__(self):

        self.tela()
        self.tela_menu()
        self.root.mainloop()

    def tela(self):
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('Sistema de Gerenciamento')
        self.root.config(bg='white')
        self.root.resizable(False,False)

    def tela_menu(self):
        
        # Função Cadastro
        def tela_cadastro():
            frame_login.pack_forget()

            #Frame
            frame_cadastro = tk.Frame(self.root,bg='#d4fcdd',width=400,height=400)
            frame_cadastro.pack(side='right')
            
            #Label
            texto_label = tk.Label(frame_cadastro,text='Cadastro  - Sistema de Gerenciamento',font=('Arial',12,'bold'),bg='#d4fcdd')
            texto_label.place(width=300,height=30, x = 50, y = 5)

            nome_label = tk.Label(frame_cadastro,text='Nome Completo:',font=('Arial',12,'bold'),bg='#d4fcdd')
            nome_label.place(width=160,height=30,x = 10, y = 60)

            email_label = tk.Label(frame_cadastro,text='Email:',font=('Arial',12,'bold'),bg='#d4fcdd')
            email_label.place(width=60,height=30,x = 20, y = 110)

            senha_label = tk.Label(frame_cadastro,text='Senha:',font=('Arial',12,'bold'),bg='#d4fcdd')
            senha_label.place(width=60,height=30,x = 20, y = 160)

            senha_confirmacao_label = tk.Label(frame_cadastro,text='Confirme a senha:',font=('Arial',12,'bold'),bg='#d4fcdd')
            senha_confirmacao_label.place(width=150,height=30,x = 20, y = 210)

            sexo = tk.Label(frame_cadastro,text='Sexo:',font=('Arial',12,'bold'),bg='#d4fcdd')
            sexo.place(width=60,height=30,x = 20, y = 260)

            uh = tk.Label(frame_cadastro,text='UH:',font=('Arial',12,'bold'),bg='#d4fcdd')
            uh.place(width=40,height=30,x = 20, y = 310)

            fazer_login_label = tk.Label(frame_cadastro,text='Já tem uma conta?',bg='#d4fcdd',font=('Arial',11,'bold'))
            fazer_login_label.place(width=200,height=20,x = 80, y = 360)

            # Input

            nome_cadastro_entry = tk.Entry(frame_cadastro,justify='left',relief='flat',border=2,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
            nome_cadastro_entry.place(width=200,height=24,x = 160, y = 63)

            email_cadastro_entry = tk.Entry(frame_cadastro,justify='left',relief='flat',border=2,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
            email_cadastro_entry.place(width=200,height=24,x = 100, y = 113)

            senha_cadastro_entry = tk.Entry(frame_cadastro,justify='left',relief='flat',border=2,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
            senha_cadastro_entry.place(width=200,height=24,x = 100, y = 163)

            senha_confirmacao_cadastro_entry = tk.Entry(frame_cadastro,justify='left',relief='flat',border=2,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
            senha_confirmacao_cadastro_entry.place(width=200,height=24,x = 170, y = 213)

            # Radio

            sexo_f_escolha = tk.Radiobutton(frame_cadastro,text='Feminino',font=('Arial',10,'bold'),bg='#d4fcdd',relief='flat',value=0)
            sexo_f_escolha.place(width=100,height=30,x = 80, y = 260)

            sexo_m_escolha = tk.Radiobutton(frame_cadastro,text='Masculino',font=('Arial',10,'bold'),bg='#d4fcdd',relief='flat',value=1)
            sexo_m_escolha.place(width=100,height=30,x = 190, y = 260)

            # Style ttk

            estilo  = ttk.Style()
            estilo.configure('TCombobox',relief='flat',selectforeground = 'black',selectbackground = 'white')

            #ComboBox

            uh_list = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','DF']

            uh_escolha = ttk.Combobox(frame_cadastro, values=uh_list,style='TCombobox',state = 'readonly',background='white')
            uh_escolha.set("Estados")
            uh_escolha.place(width=100, height=20,x = 60, y = 314)

            # Button
            
            botao_login_cadastro = tk.Button(frame_cadastro,text='Entrar',bg='#68d5fc',font=('Arial',11,'bold'),border=1,activebackground='#b4e7fa',bd=1)
            botao_login_cadastro.place(width=100,height=26,x = 260, y = 355 )

            # Fim da função

        # Frame

        frame_logo = tk.Frame(self.root,bg = 'white',width=200,height=400)
        frame_logo.pack(side='left')

        frame_login = tk.Frame(self.root,bg='#d4fcdd',width=400,height=400)
        frame_login.pack(side='right')
    
        # Imagem

        img = Image.open('assets/imagens/logo.png')
        imagem_logo = ImageTk.PhotoImage(img)
        imagem = tk.Label(frame_logo,image=imagem_logo)
        imagem.image = imagem_logo
        imagem.pack(padx=30)

        # Label

        texto_label = tk.Label(frame_login,text='Sistema de Gerenciamento',font=('Arial',14,'bold'),bg='#d4fcdd')
        texto_label.place(width=240,height=30, x = 90, y = 15)

        email_label = tk.Label(frame_login,text='Email',font=('Arial',14,'bold'),bg='#d4fcdd')
        email_label.place(width=60,height=30,x = 40, y = 70)

        senha_label = tk.Label(frame_login,text='Senha',font=('Arial',14,'bold'),bg='#d4fcdd')
        senha_label.place(width=60,height=30,x = 40, y = 150)

        cadastre_label = tk.Label(frame_login,text='Não tem uma conta?',bg='#d4fcdd',font=('Arial',11,'bold'))
        cadastre_label.place(width=200,height=20,x = 60, y = 360)

        # Entry

        email_entry = tk.Entry(frame_login,justify='left',relief='flat',border=2,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
        email_entry.place(width=260,height=26,x = 60, y = 108)

        senha_entry = tk.Entry(frame_login,show='*',relief='flat',border=1,bd=6,highlightcolor='green',highlightthickness=1,insertofftime=600)
        senha_entry.place(width=260,height=26,x = 60, y = 188)

        # Checkbox
        lembrar = tk.Checkbutton(frame_login,text='Lembrar de mim',bg='#d4fcdd',activebackground='#d4fcdd',bd=0)
        lembrar.place(x = 60, y = 250)

        # Button
        
        botao_esqueceu_senha = tk.Button(frame_login,text='Esqueceu sua senha ?',bg='#d4fcdd',font=('Arial',10),activebackground='#d4fcdd',relief='flat',border=0)
        botao_esqueceu_senha.place(width=160,height=20,x = 160, y = 216)

        botao_login = tk.Button(frame_login,text='Entrar',bg='#45f588',font=('Arial'),border=1,activebackground='#5eff9c',bd=1)
        botao_login.place(width=100,height=26,x = 150, y = 300 )

        botao_cadastro = tk.Button(frame_login,text='Cadastre-se',bg='#68d5fc',font=('Arial',11,'bold'),border=1,activebackground='#b4e7fa',bd=1,command=tela_cadastro)
        botao_cadastro.place(width=100,height=26,x = 260, y = 355 )

TelaLogin()

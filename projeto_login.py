import tkinter as tk

banco = {"Ana": "a1b2c3",
        "Isabela": "12345",
        "Marcos": "amanda213",
    }   

import tkinter as tk

from tkinter import (ttk, messagebox)

janela = tk. Tk()
janela.geometry("500x600")
janela.title("LOGIN DO USUÁRIO")

login = tk.Label(janela, text = "LOGIN", font=('Arial', 40)).pack()

email_ = tk.Label(janela, text = "DIGITE SEU E-MAIL").pack(pady='40')
email_user = tk.Entry(janela)
email_user.pack()

senha_ = tk.Label(janela, text = "DIGITE SUA SENHA").pack(pady='40')
senha_user = tk.Entry(janela, show='*')
senha_user.pack()


def funcao():
    email = email_user.get()
    senha = senha_user.get()
    achei_usuario = False
    for nome, senha_bd in banco.items():
        if(nome == email) and (senha_bd == senha):
            achei_usuario = True
            messagebox.showinfo('APROVADO', "Acesso Autorizado")
            break
    if not achei_usuario:
        messagebox.showerror('ERRO', "Acesso Não Autorizado ")

button = tk.Button(janela, text="Clique aqui", command = funcao)
button.pack()

janela.mainloop()
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('600x400')
root.title('Sistema de Gerenciamento')
root.config(bg='#d4fcdd')


tv = ttk.Treeview(root,columns=('id','nome','telefone','email'),show='headings')
tv.column('id',minwidth=50,width=50)
tv.column('nome',minwidth=100,width=100)
tv.column('telefone',minwidth=100,width=100)
tv.column('email',minwidth=100,width=200)

tv.heading('id',text='ID')
tv.heading('nome',text='Nome')
tv.heading('telefone',text='Telefone')
tv.heading('email',text='Email')

tv.insert('','end',values=(1,'Matheus','(99) 99999-9999','email@email.com'))

tv.pack(pady=20)


root.mainloop()
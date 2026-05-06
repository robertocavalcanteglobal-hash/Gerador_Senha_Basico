# programa para gerenciar senhas e random
#Importar a biblioteca random para gerar senha aleatória e a biblioteca tkinter
import random
from tkinter import messagebox
from tkinter import *

#Define o interface do usuario
password_gen  = Tk()
password_gen.geometry("350x200")
password_gen.title("PythonGeeks Password Generator")

#Senha de caracteres a ser gerada
def generate_password():
 try:
   repeat = int(repeat_entry.get())
   length = int(length_entry.get())
 except:
   messagebox.showerror(message="Please key in the required inputs")
   return
 #Checar os inputs, se o comprimento da senha for menor que 1 ou 0 número de  caracteres.
 if repeat == 1:
   password = random.sample(character_string,length)
 else:
   password = random.choices(character_string,k=length)
 #Desde a senha gerada é uma lista, juntamos as caracteres para formar uma string
 password=''.join(password)
 #Declare a string
 password_v = StringVar()
 password="Created password: "+ str(password)
 #Assign the password to the declared string variables
 password_v.set(password)
 #Criação de label para mostrar a senha gerada
 password_label = Entry(password_gen, bd=0, bg="gray85", textvariable= password_v, state="readonly")
 password_label.place(x=10, y=140, height=50, width=320)

 #Defini a string de caracteres a ser usada para gerar a senha
character_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#Mention the title of the app
title_label = Label(password_gen, text="Gerador de senha", font=('Ubuntu Mono',12))
title_label.pack()
#Read length
length_label = Label(password_gen, text="entrar: ")
length_label.place(x=20,y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190,y=30)
#Read repetition
repeat_label = Label(password_gen, text="Repetição? 1: sem repetição, 2: com repetição" )
repeat_label.place(x=20,y=60)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300,y=60)

#Generate password
password_button = Button(password_gen, text="Gerador de senha", command=generate_password)
password_button.place(x=100,y=100)
#Exit and close the app
password_gen.mainloop()
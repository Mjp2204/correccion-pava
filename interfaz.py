from customtkinter import CTk, CTkButton, CTkEntry, CTkCheckBox, CTkFrame, CTkLabel
from usuario import *
from programador import Programador
import os
import sys

ruta_logo = ('imagenes/logo.png')
c_negro = '#010101'
c_blanco = '#FFFFFF'
user_data_file = 'info.txt'


root = CTk()
root.title('Programador De Tareas')
root.geometry('500x600')
root.minsize(400,500)
root.config(bg=c_negro)


frame = CTkFrame(root, bg_color= c_negro)
frame.grid(column = 0, row = 0, sticky = 'nsew', padx = 50, pady = 50)
CTkLabel(root, image= ruta_logo).grid(columnspan= 2, row= 0)

root.columnconfigure(0, weight =1)
root.rowconfigure(0, weight = 1)



root.mainloop()

import csv
from tkinter import *
from tkinter import messagebox as mss
import os 
import modulos.modalidad_juego as MJ
import pandas as pd

class Windows_registro():
	def __init__(self):
		self.pantalla_registro()

	def pantalla_registro(self):
		self.ventana = Tk()
		self.ventana.title('Registro de usuario')
		self.ventana.config(bg='cyan')
		self.ventana.geometry("200x270")

		l3 = Label(self.ventana,text='Usuario')
		l3.place(x=67,y=17)
		l3.config(bg='cyan')

		self.e1= Entry(self.ventana,width=15)
		self.e1.place(x=25,y=40)

		l4 = Label(self.ventana, text='Contrasena')
		l4.place(x=54,y=76)
		l4.config(bg='cyan')

		self.e2 = Entry(self.ventana,width=15)
		self.e2.place(x=25, y=95)

		l5 = Label(self.ventana, text='Re-Contrasena')
		l5.place(x=50,y=133)
		l5.config(bg='cyan')

		self.e3 = Entry(self.ventana,width=15)
		self.e3.place(x=25, y=155)

		b1= Button(self.ventana, text='Registrar', command= self.creacion_registro)
		b1.place(x=60,y=200)

		self.ventana.mainloop()

	def creacion_registro(self):
		self.t1 = self.e1.get()
		self.t2 = self.e2.get()
		self.t3 = self.e3.get()

		sfile = 'usuarios/'+str(self.t1)+'.csv'
		if os.path.exists(sfile):
			mss.showinfo(message='El nombre del usuario ya existente',
				title='Registro')
			self.e1.delete(0,END)
			self.e2.delete(0,END)
			self.e3.delete(0,END)
		else:
			if str(self.t2)==str(self.t3):
			
				usuario=str(self.t1)
				if not os.path.exists('usuarios/'):
					os.makedirs('usuarios/')

					datos=[['Contrasena','Personaje','Nivel'],[str(self.t2), "", 0]]
					df=pd.DataFrame(datos)
					print(df)

					df.to_csv('usuarios/'+usuario+'.csv',index=False,header=False)
					self.ventana.destroy()
					
					MJ.Modalidad(usuario)
				else:
					datos=[['Contrasena','Personaje','Nivel'],[str(self.t2), "", 0]]
					df=pd.DataFrame(datos)
					print(df)
					df.to_csv('usuarios/'+usuario+'.csv',index=False,header=False)

					mss.showinfo(message='Registro Exitoso',title='Registro')
					self.ventana.destroy()
					MJ.Modalidad(usuario)
			else:
				mss.showinfo(message='Las contraseñas no coinciden',
				title='Registro')
				self.e2.delete(0,END)
				self.e3.delete(0,END)


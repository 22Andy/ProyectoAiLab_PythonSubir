from tkinter import *
import pandas as pd
from tkinter import messagebox as mss
import os
import modulos.registrarse as RE
import modulos.modalidad_juego as MJ

class Window_iniciar_sesion():
	def __init__(self):
		self.pantalla_sesion()

	def pantalla_sesion(self):

		self.ventana = Tk()
		self.ventana.title('Inicio de sesión')
		self.ventana.config(bg='pink')
		
		self.l3 = Label(self.ventana,text='Usuario')
		self.l3.place(x=67,y=15)
		self.l3.config(bg='pink')

		self.e1= Entry(self.ventana,width=15)
		self.e1.place(x=25,y=40)

		self.l4 = Label(self.ventana, text='Contrasena')
		self.l4.place(x=54,y=70)
		self.l4.config(bg='pink')

		self.e2 =Entry(self.ventana,width=15)
		self.e2.place(x=25,y=95)

		b = Button(self.ventana, text='Iniciar', command=self.verificar)
		b.place(x=60,y=150)

		self.ventana.mainloop()

	def lector(self, direccion):
		data = pd.read_csv(direccion)
		return data

	def verificar(self):
		usuario =  str(self.e1.get())
		sfile = 'usuarios/'+usuario+'.csv'

		# sí existe un archivo que tiene el nombre del usario
		if os.path.exists(sfile):
			info_jugador = self.lector(sfile)
			contrasena = str(info_jugador.loc[0,'Contrasena'])

			if contrasena== str(self.e2.get()):
				self.ventana.destroy()
				MJ.Modalidad(usuario)
			else:
				print(contrasena== str(self.e2.get()), type(contrasena), type(str(self.e2.get())))
				mss.showinfo(message='Contrasena incorrecta',title='Verificación')
				self.e2.delete(0,END)
		else:
			resp=mss.askokcancel(message='No se encontro el usuario,Quiere registrar un nuevo usuario?',title='Usuario no encontrado')
			if resp==True:
				self.ventana.destroy()
				RE.Windows_registro()
			else:
				self.e1.delete(0,END)
				self.e2.delete(0,END)
from tkinter import *
import pandas as pd
import modulos.modo_historia as MH
import modulos.modo_entrenamiento as ME

class Modalidad():
	def __init__(self, usuario):
		self.usuario=usuario

		self.configuracion()

	def configuracion(self):
		self.ventana = Tk()
		self.ventana.title('Modalidad de juego')
		self.ventana.config(bg='yellow')
		self.ventana.geometry("240x150")
		b1= Button(self.ventana, text='Modo entrenamiento', command= lambda:self.entrenamiento())
		b1.place(x=40,y=40)
		b2= Button(self.ventana, text='Modo historia', command= lambda: self.historia())
		b2.place(x=60,y=90)
		self.ventana.mainloop()

	def entrenamiento(self):
		self.ventana.destroy()
		ME.entrenamiento()
		

	def historia(self):
		self.ventana.destroy()
		#data = pd.read_csv("usuarios/"+usuario+".csv", index_col=[0])
		#data.loc[usuario,'Nivel']
		MH.historia(self.usuario)
	

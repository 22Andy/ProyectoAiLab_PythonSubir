from tkinter import *
from tkinter import messagebox as mss
from PIL import ImageTk, Image
import modulos.juego_modo_historia as JMH
import pandas as pd

class historia():

	def __init__(self,usuario):
		self.usuario = usuario

		Tipo = {'Aquarder':"Agua", 'Firesor':"Fuego",
		'Mousebug':"Escarabajo",'Electder':"Eléctrico", 'Splant':"Planta", "Rockdog":"Roca"} 

		data_usuario  = pd.read_csv("usuarios/"+self.usuario+".csv")

		if int(data_usuario.loc[0,'Nivel'])>0:
			self.nombre1 = str(data_usuario.loc[0,'Personaje']) 
			self.tipo1   = Tipo[self.nombre1]  		
			JMH.Combate_historia(self.usuario, self.nombre1,self.tipo1,data_usuario.loc[0,'Nivel'])
		else:
			self.nombre1    = ""
			self.tipo1      = ""
			self.nivel      = 0

			self.ventana_inicio()
	

	def images(self, name):
		tam = (100,100)
		
		if name=='Aquarder':
			Im  = Image.open("aquarder.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		elif name=='Electder':
			Im  = Image.open("electder.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		elif name=='Firesor':
			Im  = Image.open("Firesor.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		elif name=='Mousebug':
			Im  = Image.open("mousebug.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		elif name=='Splant':
			Im  = Image.open("splant.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		else:
			Im  = Image.open("rockdog.png")
			Imt = Im.resize(tam)
			im  = ImageTk.PhotoImage(Imt)
		return im

	def iniciar(self):
		self.ventana.destroy()
		JMH.Combate_historia(self.usuario, self.nombre1,self.tipo1,self.nivel)

	def ventana_inicio(self):
		#messagebox.showinfo(message="Selecciona tu personaje con el que jugaras", title="Personaje")
		
		self.ventana = Tk()
		self.ventana.title('Elige tu personaje')
		self.ventana.geometry("370x380")
		self.ventana.config(bg='pink')

		self.l1=Label(self.ventana,text='Aquarder')
		self.l1.place(x=24,y=5)
		self.l1.config(bg='pink')

		img_1 = self.images('Aquarder')
		self.b1=Button(self.ventana, image=img_1,bd=0,bg='pink',command= lambda: self.Aquarder())
		self.b1.place(x=6,y=25)
		self.b1d=Button(self.ventana, text='Detalle',command= lambda: self.detalles_Aquarder(img_1))
		self.b1d.place(x=22,y=137)

		self.l2=Label(self.ventana,text='Electder')
		self.l2.place(x=160,y=5)
		self.l2.config(bg='pink')

		img_2 = self.images('Electder')
		self.b2=Button(self.ventana, image= img_2 ,bd=0,bg='pink',command= lambda:  self.Electder())
		self.b2.place(x=131,y=25)
		self.b2d=Button(self.ventana, text='Detalle',command= lambda:  self.detalles_Electder(img_2))
		self.b2d.place(x=142,y=137)


		self.l3=Label(self.ventana,text='Firesor')
		self.l3.place(x=280,y=5)
		self.l3.config(bg='pink')
		img_3 = self.images('Firesor')
		self.b3=Button(self.ventana, image= img_3 ,bd=0,bg='pink',command= lambda: self.Firesor())
		self.b3.place(x=256,y=25)
		self.b3d=Button(self.ventana, text='Detalle', command= lambda: self.detalles_Firesor(img_3))
		self.b3d.place(x=272,y=137)

		self.l4=Label(self.ventana,text='Mousebug')
		self.l4.place(x=23,y=170)
		self.l4.config(bg='pink')
		img_4 = self.images('Mousebug')
		self.b4=Button(self.ventana, image= img_4 ,bd=0,bg='pink',command= lambda: self.Mousebug())
		self.b4.place(x=6,y=190)
		self.b4d=Button(self.ventana, text='Detalle', command=lambda:  self.detalles_Mousebug(img_4))
		self.b4d.place(x=22,y=300)


		self.l5=Label(self.ventana,text='Splant')
		self.l5.place(x=152,y=170)
		self.l5.config(bg='pink')
		img_5 = self.images('Splant')
		self.b5=Button(self.ventana, image= img_5 ,bd=0,bg='pink',command=lambda:  self.Splant())
		self.b5.place(x=131,y=190)
		self.b5d=Button(self.ventana, text='Detalle',command= lambda: self.detalles_Splant(img_5))
		self.b5d.place(x=144,y=300)

		self.l6=Label(self.ventana,text='Rockdog')
		self.l6.place(x=285,y=170)
		self.l6.config(bg='pink')

		img_6 = self.images('Rockdog')
		self.b6=Button(self.ventana, image=img_6 ,bd=0,bg='pink',command= lambda: self.Rockdog())
		self.b6.place(x=256,y=190)
		self.b6d=Button(self.ventana, text='Detalle', command= lambda:  self.detalles_Rockdog(img_6))
		self.b6d.place(x=278,y=300)

		self.inicio=Button(self.ventana, text='INICIAR',state=DISABLED, command= lambda: self.iniciar())
		self.inicio.place(x=144,y=335)

		self.ventana.mainloop()

	#funciones que muestran los detalles de cada personaje
	def detalles_Aquarder(self,im1):
		det = Toplevel()
		det.title("Aquarder")
		per = Label(det,image=im1)
		per.grid(row=0, column=0)
		info=Label(det, text='''Aquarder: Tipo Agua\n
	    Ventaja con: Roca, Fuego\n
	    Desventaja con: Eléctrico, Planta\n
	    Normal con: Agua, Escarabajo\n\n
	    Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|
	    Aqua-jet    |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	    Cola ferrea |2 pt|
	    Cabezazo    |2 pt|
	    Lluvia      | Potenciador de campo, 1 vez cada 3 turnos.
	              | tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",16))
		info.grid(row=1,column=0)

	def detalles_Electder(self,im2):
		det = Toplevel()
		det.title("Electder")
		per = Label(det,image=im2)
		per.grid(row=0, column=0)
		info=Label(det, text='''Electder: Tipo eléctrico\n
	Ventaja con: Agua, Escarabajo\n
	Desventaja con: Roca, Planta\n
	Normal con: Eléctrico, Fuego\n\n
	Habilidad       |norm|At vent|At desv|pot norm|pot vent|pot desv|
	Trueno          |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	Arañazo         |3 pt|                                           
	Mordisco        |3 pt|                                                     
	Campo magnético | Potenciador de campo, 1 vez cada 3 turnos.
	          |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
		info.grid(row=1,column=0)


	def detalles_Firesor(self,im3):
		det = Toplevel()
		det.title("Firesor")
		per = Label(det,image=im3)
		per.grid(row=0, column=0)
		info=Label(det, text='''Firesor: Tipo fuego\n
	Ventaja con: Planta, Escarabajo\n
	Desventaja con: Agua, Roca\n
	Normal con: Eléctrico, Fuego\n\n
	Habilidad  |norm|At vent|At desv|pot norm|pot vent|pot desv|
	Llamarada  |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	Embestida  |2 pt|                                           
	Mordisco   |2 pt|                                                     
	Día soleado| Potenciador de campo, 1 vez cada 3 turnos.
	           |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
		info.grid(row=1,column=0)


	def detalles_Mousebug(self,im4):
		det = Toplevel()
		det.title("Mousebug")
		per = Label(det,image=im4)
		per.grid(row=0, column=0)
		info=Label(det, text='''Mousebug: Tipo escarabajo\n
	Ventaja con: Planta, Roca\n
	Desventaja con: Fuego, Eléctrico\n
	Normal con: Escarabajo, Agua\n\n
	Habilidad |norm|At vent|At desv|pot norm|pot vent|pot desv|
	Picotazo  |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	Embestida |2 pt|                                           
	Cabezazo  |2 pt|                                                     
	Esporas   | Potenciador de campo, 1 vez cada 3 turnos.
	          |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
		info.grid(row=1,column=0)

	def detalles_Splant(self,im5):
		det = Toplevel()
		det.title("Splant")
		per = Label(det,image=im5)
		per.grid(row=0, column=0)
		info=Label(det, text='''Splant: Tipo planta\n
	Ventaja con: Roca, Agua, Eléctrico\n
	Desventaja con: Fuego, Escarabajo\n\n
	Normal con: Planta\n
	Habilidad   |norm|At vent|At desv|pot norm|pot vent|pot desv|
	Hoja navaja |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	Mordisco    |2 pt|                                           
	Cabezazo    |2 pt|                                                     
	Rayo solar  | Potenciador de campo, 1 vez cada 3 turnos.
	          |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
		info.grid(row=1,column=0)


	def detalles_Rockdog(self,im6):
		det = Toplevel()
		det.title("Rockdog")
		per = Label(det,image=im6)
		per.grid(row=0, column=0)
		info=Label(det, text='''Rockdog: Tipo roca\n
	Ventaja con: Fuego, Eléctrico\n
	Desventaja con: Agua, Planta\n
	Normal con: Roca, Escarabajo\n\n
	Habilidad     |norm|At vent|At desv|pot norm|pot vent|pot desv|
	Roca afiliado |3 pt|   5 pt|  2 pt |  5pt   |  7 pt  |  4 pt  |
	Velocidad     |2 pt|                                           
	Cola ferrea   |2 pt|                                                     
	Campo rocoso  | Potenciador de campo, 1 vez cada 3 turnos.
	          |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
		info.grid(row=1,column=0)

	def Aquarder(self):
		self.nombre1   = "Aquarder"
		self.tipo1     = "Agua"

		self.b1.config(bg='red')

		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo para iniciar el juego?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""
			
	def Electder(self):

		self.nombre1   = "Electder"
		self.tipo1     = "Eléctrico"

		self.b2.config(bg='red')
	
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""

	def Firesor(self):
		self.nombre1   = "Firesor"
		self.tipo1     = "Fuego"
		
		self.b3.config(bg='red')
	
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo para iniciar el juego?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""

	def Mousebug(self):

		self.nombre1   = "Mousebug"
		self.tipo1     = "Escarabajo"

		self.b4.config(bg='red')
			
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo para iniciar el juego?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""

	def Splant(self):
		self.nombre1   = "Splant"
		self.tipo1     = "Planta"
			
		self.b5.config(bg='red')
		
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo para iniciar el juego?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""


	def Rockdog(self):

		self.nombre1   = "Rockdog"
		self.tipo1     = "Roca"

		self.b6.config(bg='red')
		
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)

		resp = mss.askyesno(message='Listo para iniciar el juego?',title='Comenzamos')
		if resp==True:
			self.inicio.config(state=NORMAL)
		else:
			self.b1.config(state=NORMAL,bg='pink')
			self.b2.config(state=NORMAL,bg='pink')
			self.b3.config(state=NORMAL,bg='pink')
			self.b4.config(state=NORMAL,bg='pink')
			self.b5.config(state=NORMAL,bg='pink')
			self.b6.config(state=NORMAL,bg='pink')
			self.nombre1    = ""
			self.tipo1      = ""
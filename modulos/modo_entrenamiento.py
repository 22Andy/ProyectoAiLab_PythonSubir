from tkinter import *
from tkinter import messagebox as mss
from PIL import ImageTk, Image
import modulos.juego_modo_entrenamiento as MJE

# redimension de las imagenes
def images(name):
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



#funciones que muestran los detalles de cada personaje
def detalles_Aquarder(im1):
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


def detalles_Electder(im2):
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
Arañazo         |2 pt|                                           
Mordisco        |2 pt|                                                     
Campo magnético | Potenciador de campo, 1 vez cada 3 turnos.
          |tiene una duracion de 2 turnos.''',anchor="w",font=("Courier",15))
	info.grid(row=1,column=0)

def detalles_Firesor(im3):
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


def detalles_Mousebug(im4):
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


def detalles_Splant(im5):
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


def detalles_Rockdog(im6):
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


# Declaracion de valiables globales


def Aquarder():
	global band
	global nombre1
	global nombre2
	global Personaje
	global Rival
	global tipo1
	global tipo2,b1,b2,b3,b4,b5,b6,ventana1

	if band==0:
		nombre1   = "Aquarder"
		tipo1     = "Agua"
		band      = 1
		Personaje = 1
		# pongo en rojo la ventana del primer personaje
		b1.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==1:
			b1.config(bg="green")
		else:
			b1.config(bg='blue')
		nombre2 = "Aquarder"
		tipo2 = "Agua"
		band  = 2
		Rival = 1
		
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0



def Electder():
	global band
	global nombre1
	global nombre2
	global tipo1
	global tipo2
	global Personaje
	global Rival,b1,b2,b3,b4,b5,b6,ventana1

	if band==0:
		nombre1   = "Electder"
		tipo1     = "Eléctrico"
		band      = 1
		Personaje = 2
		b2.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==2:
			b2.config(bg='green')
		else:
			b2.config(bg='blue')
		nombre2  = "Electder"
		tipo2    = "Eléctrico"
		band     = 2
		Rival    = 2
		
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0




def Firesor():
	global band
	global nombre1
	global nombre2
	global tipo1
	global tipo2
	global Personaje
	global Rival,b1,b2,b3,b4,b5,b6,ventana1
	if band==0:
		nombre1   = "Firesor"
		tipo1     = "Fuego"
		band      = 1
		Personaje = 3
		# pongo en rojo la ventana del primer personaje
		b3.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==3:
			b3.config(bg='green')
		else:
			b3.config(bg='blue')
		nombre2 = "Firesor"
		tipo2   = "Fuego"
		band    = 2
		Rival   = 3
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0

def Mousebug():
	global band
	global nombre1
	global nombre2
	global tipo1
	global tipo2
	global Personaje
	global Rival,b1,b2,b3,b4,b5,b6,ventana1

	if band==0:
		nombre1   = "Mousebug"
		tipo1     = "Escarabajo"
		band      = 1
		Personaje = 4
		b4.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==4:
			b4.config(bg='green')
		else:
			b4.config(bg='blue')
		nombre2  = "Mousebug"
		tipo2    = "Escarabajo"
		band     = 2
		Rival    = 4
		
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0

def Splant():
	global band
	global nombre1
	global nombre2
	global tipo1
	global tipo2
	global Personaje
	global Rival,b1,b2,b3,b4,b5,b6,ventana1

	if band==0:
		nombre1   = "Splant"
		tipo1     = "Planta"
		band      = 1
		Personaje = 5
		b5.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==5:
			b5.config(bg='green')
		else:
			b5.config(bg='blue')
		nombre2 = "Splant"
		tipo2   = "Planta"
		band    = 2
		Rival   = 5
		
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0


def Rockdog():
	global band
	global nombre1
	global nombre2
	global tipo1
	global tipo2
	global Personaje
	global Rival,b1,b2,b3,b4,b5,b6,ventana1


	if band==0:
		nombre1   = "Rockdog"
		tipo1     = "Roca"
		Personaje = 6
		band      = 1 
		b6.config(bg='red')
		messagebox.showinfo(message="Selecciona el contrincante", title="Contrincate")
	else:
		if Personaje==6:
			b6.config(bg='green')
		else:
			b6.config(bg='blue')
		nombre2 = "Rockdog"
		tipo2   = "Roca"
		band    = 2
		Rival   = 6
		
		b1.config(state=DISABLED)
		b2.config(state=DISABLED)
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b5.config(state=DISABLED)
		b6.config(state=DISABLED)
		resp=mss.askyesno(message='Listo?',title='Comenzamos')
		if resp==True:
			inicio.config(state=NORMAL)
		else:
			b1.config(state=NORMAL,bg='pink')
			b2.config(state=NORMAL,bg='pink')
			b3.config(state=NORMAL,bg='pink')
			b4.config(state=NORMAL,bg='pink')
			b5.config(state=NORMAL,bg='pink')
			b6.config(state=NORMAL,bg='pink')
			Personaje  = 0
			nombre1    = ""
			nombre2    = ""
			Rival      = 0
			tipo1      = ""
			tipo2      = ""
			band       = 0

def iniciar():
	ventana1.destroy()
	MJE.Combate_entrenamiento( nombre1, nombre2, tipo1, tipo2)

def entrenamiento():

	global ventana1, b1,b2,b3,b4,b5,b6, Personaje, nombre1, nombre2, Rival, tipo1, tipo2, band,inicio

	Personaje  = 0
	nombre1    = ""
	nombre2    = ""
	Rival      = 0
	tipo1      = ""
	tipo2      = ""
	band       = 0


	ventana1 = Tk()
	ventana1.title('Elige los perosnajes para la batalla')
	ventana1.geometry("370x380")
	ventana1.config(bg='pink')

	l1=Label(ventana1,text='Aquarder')
	l1.place(x=24,y=5)
	l1.config(bg='pink')
	im1 = images("Aquarder")
	b1=Button(ventana1, image=im1,bd=0,bg='pink',command=Aquarder)
	b1.place(x=6,y=25)
	b1d=Button(ventana1, text='Detalle',command= lambda: detalles_Aquarder(im1))
	b1d.place(x=22,y=137)

	l2=Label(ventana1,text='Electder')
	l2.place(x=160,y=5)
	l2.config(bg='pink')
	im2 = images("Electder")
	b2=Button(ventana1, image=im2 ,bd=0,bg='pink',command=Electder)
	b2.place(x=131,y=25)
	b2d=Button(ventana1, text='Detalle',command= lambda:detalles_Electder(im2))
	b2d.place(x=142,y=137)

	l3=Label(ventana1,text='Firesor')
	l3.place(x=280,y=5)
	l3.config(bg='pink')
	im3 = images("Firesor")
	b3=Button(ventana1, image=im3 ,bd=0,bg='pink',command=Firesor)
	b3.place(x=256,y=25)
	b3d=Button(ventana1, text='Detalle', command=lambda:detalles_Firesor(im3))
	b3d.place(x=272,y=137)

	l4=Label(ventana1,text='Mousebug')
	l4.place(x=23,y=170)
	l4.config(bg='pink')
	im4 = images("Mousebug")
	b4=Button(ventana1, image=im4 ,bd=0,bg='pink',command=Mousebug)
	b4.place(x=6,y=190)
	b4d=Button(ventana1, text='Detalle', command= lambda: detalles_Mousebug(im4))
	b4d.place(x=22,y=300)

	l5=Label(ventana1,text='Splant')
	l5.place(x=152,y=170)
	l5.config(bg='pink')
	im5 = images("Splant")
	b5=Button(ventana1, image=im5 ,bd=0,bg='pink',command=Splant)
	b5.place(x=131,y=190)
	b5d=Button(ventana1, text='Detalle',command=lambda:detalles_Splant(im5))
	b5d.place(x=144,y=300)

	l6=Label(ventana1,text='Rockdog')
	l6.place(x=285,y=170)
	l6.config(bg='pink')
	im6 = images("Rockdog")
	b6=Button(ventana1, image=im6 ,bd=0,bg='pink',command=Rockdog)
	b6.place(x=256,y=190)
	b6d=Button(ventana1, text='Detalle', command= lambda:detalles_Rockdog(im6))
	b6d.place(x=278,y=300)

	inicio=Button(ventana1, text='INICIAR',state=DISABLED,command= iniciar)
	inicio.place(x=144,y=335)
	ventana1.mainloop()

	
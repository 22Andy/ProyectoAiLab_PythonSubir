from tkinter import *
import pandas as pd
from tkinter import messagebox as mss
from PIL import ImageTk, Image
import modulos.modalidad_juego as MJ
import random
import time
import os
import tkinter.font as tkFont

class Combate_historia():
	def __init__(self,usuario,nombre1,tipo1,nivel):
		self.nombre1   = nombre1
		self.tipo1     = tipo1
		self.nombre2   = ""
		self.tipo2     = ""
		self.usuario   = usuario

		self.data_usuario  = pd.read_csv("usuarios/"+usuario+".csv")
		self.nivel         = nivel

		# aqui ya tenemos lleno la información de con quien nos toca cambatir
		# en modo historia
		self.Rival(self.nivel)

		self.puntaje_personaje = 25.0
		self.puntaje_rival     = 25.0
		self.band_pot1         = "Desactivado"
		self.band_pot2         = "Desactivado"
		self.contador_poten1   = 0
		self.contador_poten2   = 0

		Aquarder= {'Potenciador':'Lluvia', 'Ventajas':{'Roca','Fuego'},
		'Desventajas':{'Eléctrico','Planta'},'Normal':{'Agua','Escarabajo'}} 

		Electder= {'Potenciador':'Campo magnético', 'Ventajas':{'Agua','Escarabajo'},
		'Desventajas':{'Roca','Planta'},'Normal':{'Eléctrico','Fuego'}}

		Mousebug = {'Potenciador':'Esporas', 'Ventajas':{'Planta','Roca'},
		'Desventajas':{'Fuego','Eléctrico'},'Normal':{'Escarabajo','Agua'}}

		Splant = {'Potenciador':'Rayo solar', 'Ventajas':{'Roca','Agua','Eléctrico'},
		'Desventajas':{'Fuego','Escarabajo'},'Normal':{'Planta'}}

		Rockdog = {'Potenciador':'Campo rocoso', 'Ventajas':{'Fuego','Eléctrico'},
		'Desventajas':{'Agua','Planta'},'Normal':{'Roca','Escarabajo'}}

		Firesor = {'Potenciador':'Día soleado', 'Ventajas':{'Planta','Escarabajo'},
		'Desventajas':{'Agua','Roca'},'Normal':{'Eléctrico','Fuego'}}

		self.diccionario={'Aquarder': Aquarder,'Electder': Electder, 'Mousebug':Mousebug, 
		'Splant':Splant, 'Rockdog':Rockdog, 'Firesor':Firesor}
		
		self.pantalla_sesion()

	def Rival(self,nivel):
		'''
		A esta funcion le das el nivel en el que estas en modo historia y
		te regresa el nombre del Rival con el que te toca competir 

		'''
		if nivel==0:
			self.nombre2 = "Aquarder"
			self.tipo2   = "Agua"
		elif nivel==1:
			self.nombre2 = "Electder"
			self.tipo2   = "Eléctrico"
		elif nivel==2:
			self.nombre2 = "Firesor"
			self.tipo2   = "Fuego"
		elif nivel==3:
		    self.nombre2 = "Mousebug"
		    self.tipo2   = "Escarabajo"
		elif nivel==4:
			self.nombre2 = "Splant"
			self.tipo2   = "Planta"
		else:
			self.nombre2 = "Rockdog"
			self.tipo2   = "Roca"    


	def read_dataframe(self):
		data = pd.read_csv("ataques.csv", index_col=[0,1])
		return data

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

	def combate(self,poder):
		''' Esta funcion se encarga de llevar el conteo de la lucha que el personaje
		    hace sobre su rival
		'''
		if (poder == self.diccionario[self.nombre1]['Potenciador']) and  (self.band_pot1=="Desactivado")  and (self.contador_poten1==0):
			self.band_pot1 ='Activado'
			self.contador_poten1 = 1
			self.poten_1 = poder
			self.n.config(text=self.nombre1+''' activo '''+self.poten_1+'''\n Sus ataques se intensifican por 2 turnos''',anchor="center")
			self.a4.config(state=DISABLED)
			self.ventana.update()
			time.sleep(1)
		else:
			#Ventaja
			if self.tipo2 in self.diccionario[self.nombre1]['Ventajas']:
				
				if self.band_pot1=="Desactivado":
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n  Es efectivo!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_CV']

				else:
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n  Muy efectivo!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_CPCV']
			#Desventaja
			elif self.tipo2 in self.diccionario[self.nombre1]['Desventajas']:
				
				if self.band_pot1=="Desactivado":
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n  Nada efectivo!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_SV']
				else:
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n  Es poco efectivo!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_CPSV']
			#Normal
			else:
			# self.tipo2 in self.diccionario[self.nombre1]['Normal'] :
				if self.band_pot1=="Desactivado":
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n Es Normal!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_N']
				else:
					self.n.config(text=self.nombre1+''' a utilizado '''+poder+''' \n Es Normal con potenciador!''',anchor="center",fg='blue')
					restar=self.info_personaje.loc[poder,'A_CPN']
			self.puntaje_rival -=restar
			self.ventana.update()
			time.sleep(2)

		if self.contador_poten1!=0:
			self.contador_poten1+=1
			if self.contador_poten1==4:
				self.contador_poten1=0
				self.band_pot1 ="Desactivado"
				self.a4.config(state=NORMAL)
				self.n.config(text='''Termino el efecto '''+self.poten_1, anchor="center",fg='blue')
			else:
				self.n.config(text=self.nombre1+''' utilizo '''+self.poten_1+'''\n Le quedan '''+str(4-self.contador_poten1)+''' Movimientos''',anchor="center",fg='blue')
		fon = tkFont.Font(family="Lucida Grande", size=15)
		self.p2t.config(text=str(self.puntaje_rival)+' Hp', font = fon)
		self.ventana.update()
		time.sleep(2)

		if self.puntaje_rival<=0:
			mss.showinfo(message="GANASTE !!!!!", title="Felicitaciones")
			#self.n.config(text= " GAME OVER")
			#self.ventana.update()
			#time.sleep(2)
			#resp=mss.askyesno(message='Va a continuar jugando?',title='Continuar')
			#if resp:
			self.nivel = self.nivel+1
			if self.nivel==6:
				mss.showinfo(message="GAME OVER", title="Felicidades")
				os.remove('usuarios/'+self.usuario+'.csv')
				self.ventana.destroy()
			else:

				resp=mss.askyesno(message='Continuar?',title='seguir el modo historia')
				if resp:
					self.puntaje_personaje = 25.0
					self.puntaje_rival     = 25.0
					self.band_pot1         = "Desactivado"
					self.band_pot2         = "Desactivado"
					self.contador_poten1   = 0
					self.contador_poten2   = 0
					self.Rival(self.nivel) 
					self.ventana.destroy()
					self.pantalla_sesion()
				else:
					self.data_usuario.loc[0,'Personaje']= self.nombre1
					self.data_usuario.loc[0,'Nivel']    = self.nivel
					print("ganaste: ", self.data_usuario)
					self.data_usuario.to_csv('usuarios/'+self.usuario+'.csv',index=False)
					self.ventana.destroy()

		else:
			self.CPU()


	def CPU(self):
		self.a1.config(state=DISABLED)
		self.a2.config(state=DISABLED)
		self.a3.config(state=DISABLED)
		self.a4.config(state=DISABLED)

		#Dicc_Rival     = self.diccionario[self.nombre2]
		if (self.band_pot2=="Desactivado") and (self.contador_poten2==0):
			at_rival = random.randint(1,4)
		else:
			at_rival = random.randint(1,3)

		#Potenciador del Rival
		if at_rival==4:
			self.contador_poten2 = 1
			self.band_pot2 = "Activado"
			self.poten_2 = self.diccionario[self.nombre2]['Potenciador']
			self.n.config(text="CPU:"+self.nombre2+''' activo  '''+self.poten_2+'''\n Sus ataques se intensifican por 2 turnos''',anchor="center",fg='red')
			self.ventana.update()
			time.sleep(2)
		else:
			# nombre del ataque que aplicara el rival al personaje
			nombre_at_rival = self.info_rival.index[at_rival-1]
			# Si tipo1 esta en el conjunto de las ventajas del Rival
			if self.tipo1 in self.diccionario[self.nombre2]['Ventajas']:
				
				if self.band_pot2=='Desactivado':
					self.n.config(text="CPU: "+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n  Es efectivo!''',anchor="center", fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_CV']
					
				else:
					self.n.config(text="CPU: "+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n  Muy efectivo!''',anchor="center", fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_CPCV']

			# Si tipo1 se encuentra en el conjunto de las desventajas del Rival
			elif self.tipo1 in self.diccionario[self.nombre2]['Desventajas']:
				
				if self.band_pot2=='Desactivado':
					self.n.config(text="CPU: "+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n  Nada efectivo!''',anchor="center", fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_SV']
				else:
					self.n.config(text="CPU: "+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n  Es poco efectivo!''',anchor="center",  fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_CPSV']
			# Si tipo1 esta en el conjunto de normal
			else:
			# self.tipo1 in self.diccionario[self.nombre2]['Normal'] :
				
				if self.band_pot2=='Desactivado':
					self.n.config(text="CPU :"+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n  Normal!''',anchor="center",fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_N']
				else:
					self.n.config(text="CPU :"+self.nombre2+''' a utilizado '''+nombre_at_rival+''' \n Normal con potenciador!!''',anchor="center",fg='red')
					restar_p = self.info_rival.loc[nombre_at_rival,'A_CPN']
			self.puntaje_personaje -= restar_p
			self.ventana.update()
			time.sleep(1)

		if self.contador_poten2!=0:
			self.contador_poten2 +=1

			if self.contador_poten2==4:
				self.contador_poten2 = 0
				self.band_pot2 = 'Desactivado'
				self.n.config(text='''CPU : Termino el efecto '''+self.poten_2, anchor="center",fg='red')
			else:
				self.n.config(text="CPU :"+self.nombre2+''' utilizo '''+self.poten_2+'''\n Quedan '''+str(4-self.contador_poten2)+''' Movimientos''',anchor="center",fg='red')
		fon = tkFont.Font(family="Lucida Grande", size=15)
		self.p1t.config(text=str(self.puntaje_personaje)+" Hp",font=fon)
		self.ventana.update()
		time.sleep(1)
		# si yo pierdo
		if self.puntaje_personaje <=0:
			mss.showinfo(message=self.nombre2+" gano, es jugador de la CPU!!!", title="Felicidades")
			self.n.config(text="se acabo la batalla",fg='red' )
			self.ventana.update()
			time.sleep(2)
			self.data_usuario.loc[0,'Personaje'] = self.nombre1
			self.data_usuario.loc[0,'Nivel']     = self.nivel

			self.data_usuario.to_csv('usuarios/'+self.usuario+'.csv',index=False)
			self.ventana.destroy()
			MJ.Modalidad(self.usuario)
		else:
			self.a1.config(state=NORMAL)
			self.a2.config(state=NORMAL)
			self.a3.config(state=NORMAL)
			if self.band_pot1 =="Desactivado": 
				self.a4.config(state=NORMAL)

	def pantalla_sesion(self):

		self.ventana = Tk()
		self.ventana.geometry("400x300")
		self.ventana.config(bg='blue')	
		# leemos los puntajes de 
		data = self.read_dataframe()
		#Se saca del dataframe la informacion de los personajes que estan participando (Rival, Personaje)
		self.info_personaje = data.loc[self.nombre1]
		self.info_rival     = data.loc[self.nombre2]
		
		# Se manda el poder con el que se aplica
		self.a1 = Button(self.ventana, text=self.info_personaje.index[0],bg='red',fg='white', width=15,command= lambda : self.combate(self.info_personaje.index[0]))
		self.a1.place(x=10,y=10)
		#a1.config(state=DISABLED)

		self.a2 = Button(self.ventana, text=self.info_personaje.index[1],bg='red',fg='white', width=15,command= lambda : self.combate(self.info_personaje.index[1]))
		self.a2.place(x=10,y=40)
		#a2.config(state=DISABLED)

		self.a3 = Button(self.ventana, text=self.info_personaje.index[2],bg='red',fg='white', width=15,command= lambda : self.combate(self.info_personaje.index[2]))
		self.a3.place(x=10,y=70)
		#a2.config(state=DISABLED)

		self.a4 = Button(self.ventana, text=self.diccionario[self.nombre1]['Potenciador'],bg='red',fg='white', width=15,command= lambda: self.combate(self.diccionario[self.nombre1]['Potenciador']))
		self.a4.place(x=10,y=100)
		#a2.config(state=DISABLED)

		img_p = self.images(self.nombre1)
		
		p1=Label(self.ventana, image = img_p, bg='blue' )
		p1.place(x=140,y=10)

		fon1=tkFont.Font(family="Lucida Grande", size=14)
		p1n=Label(self.ventana, text=self.nombre1, bg='blue',font=fon1)
		p1n.place(x=140,y=120)

		fon=tkFont.Font(family="Lucida Grande", size=15)

		self.p1t=Label(self.ventana, text=str(self.puntaje_personaje)+" Hp", bg='blue',font=fon)
		self.p1t.place(x=140,y=145)

		img_r = self.images(self.nombre2)

		p2=Label(self.ventana,image = img_r , bg='blue')
		p2.place(x=280,y=10)

		p2n=Label(self.ventana, text=self.nombre2, bg='blue',font=fon1)
		p2n.place(x=280,y=120)

		self.p2t =Label(self.ventana, text=str(self.puntaje_rival)+" Hp",bg='blue',font=fon)
		self.p2t.place(x=280,y=145)

		self.n = Button(self.ventana, text="La batalla esta por iniciar",bg='pink',fg='blue', width=45)
		self.n.place(x=40,y=200)
		time.sleep(1)

		t = random.randint(1,2)
		if t==1:
			self.n.config(text="El primer movimiento es tuyo\n¡¡Piensa bien!!\n",anchor="center")
		else:
			self.n.config(text="El primer movimiento es del CPU\n¡¡Cuidado!!\n",anchor="center")
			self.ventana.update()
			time.sleep(2)
			self.CPU()
		self.ventana.mainloop()
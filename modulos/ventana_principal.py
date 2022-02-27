from tkinter import *
from tkinter import messagebox as mss
import modulos.iniciar_sesion as IN
import modulos.registrarse as RE
from PIL import ImageTk, Image

class Window1():
	def __init__(self):

		self.ventana = Tk()
		self.ventana.title('Video juego tipo pokemon')
		#self.frame =Frame(self.ventana)
		#self.frame.pack()
		Im1  = Image.open("aquarder.png")
		Im_1 = Im1.resize((300,200))
		im1  = ImageTk.PhotoImage(Im_1)
		im1_label=Label(self.ventana,image=im1)
		im1_label.place(x=0,y=0, relwidth=1, relheight=1)

		self.ventana.config(width="300",height="200")
		self.ventana.config(cursor="heart") 

		b1= Button(self.ventana, text='Iniciar sesión', command=self.Iniciar_sesion)
		b1.place(x=40,y=30)

		l1= Label(self.ventana,text='1')
		l1.place(x=190,y=30)
		l1.config(bg='red')

		b2= Button(self.ventana, text='Usuario nuevo', command= self.Registrarse)
		b2.place(x=35,y=80)

		l2= Label(self.ventana,text='2')
		l2.place(x=190,y=80)
		l2.config(bg='red')

		self.ventana.mainloop()

	def Iniciar_sesion(self):
		self.ventana.destroy()
		IN.Window_iniciar_sesion()

	def Registrarse(self):
		self.ventana.destroy()
		RE.Windows_registro()
# -*- enconding: utf-8 -*-
import parser 
from tkinter import filedialog
from tkinter import*
from tkinter import messagebox 
from PIL import Image,ImageTk

class Ventana():
	def __init__(self):
		self.ruta="none"
		self.iniciarVista()

	def iniciarVista(self):
		self.raiz=Tk()
		self.raiz.geometry('700x700')
		self.raiz.resizable(0,0)
		self.raiz.configure(background = '#10316b')

		self.titulo=Label(self.raiz,text="COMPILER JY",font=("Times", 46,"bold"),fg="#e25822",background = '#10316b').place(x=140,y=10)
		img1 = Image.open('imagenes/sacar.png')
		img1 = img1.resize((40, 40), Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.boton= Button(self.raiz,text="cargar",image=img1,fg="black",command=self.cargarArchivo)
		self.boton.place(x=10, y=95)

		img2 = Image.open('imagenes/guardar.png')
		img2 = img2.resize((40, 40), Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		self.boton= Button(self.raiz,text="guardar",image=img2,fg="black",command=self.guardarArchivo)
		self.boton.place(x=10, y=145)

		img3 = Image.open('imagenes/compilar.png')
		img3 = img3.resize((40, 40), Image.ANTIALIAS)
		img3 = ImageTk.PhotoImage(img3)
		self.boton= Button(self.raiz,text="compilar",image=img3,fg="black",command=self.compilar)
		self.boton.place(x=10, y=195)


		self.scrollbar=Scrollbar(self.raiz)
		self.scrollbar.pack(side= RIGHT, fill=Y)
		
		self.text = Text(self.raiz,width=65,height=25,fg="#e25822", background='black',insertbackground="#e25822", yscrollcommand=self.scrollbar.set)
		self.text.place(x=85,y=95)

		self.textConsol = Text(self.raiz,width=65,height=5, background='black',fg="#ececeb")
		self.textConsol.place(x=85,y=535)
		self.scrollbar.config(command=self.text.yview)

		self.raiz.mainloop()

	def cargarArchivo(self):
		self.text.delete("1.0",END)
		self.ruta = filedialog.askopenfilename(initialdir = "/home/jesus/Escritorio",title = "Select file",filetypes = (("JY files","*.JY"),("all files","*.*")))
		f = open(self.ruta, 'r')
		data = f.read()
		self.text.insert(INSERT, data)
		f.close()

	def guardarArchivo(self):
		if(self.ruta!="none"):
			f = open(self.ruta, 'w')
			f.write(self.text.get("1.0",END))
			f.close()
		else:
			self.guardarArchivo1()

	def guardarArchivo1(self):
			self.ruta=filedialog.asksaveasfile(initialdir = "/home/jesus/Escritorio",title = "Save file",filetypes = (("JY files","*.JY"),("all files","*.*")))
			aux=self.ruta
			f = open(aux, 'w')
			f.write(self.text.get("1.0",END))
			f.close()

    			
	def compilar(self):
		datos=self.text.get("1.0",END)
		parser.VERBOSE = 0
		self.borrar()
		
		try:
			parser.parser.parse(datos, tracking=True)
			self.textConsol.insert(INSERT,"COMPILADO")

		except:
			self.textConsol.insert(INSERT,"ERROR DE SINTAXIS")	

	
	def borrar(self):
    		self.textConsol.delete("1.0",END)


    				
				
			

v=Ventana()

	

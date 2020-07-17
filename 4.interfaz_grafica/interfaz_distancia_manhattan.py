# Importar la librería Tkinter
from tkinter import *
# Importar las clases de PlanoCartesiano y Punto del archivo distanciaManhattan.py
from distanciaManhattan import *

def calcularDistancia():
	A = Punto(float(ptA_X.get()), float(ptA_Y.get()))
	B = Punto(float(ptB_X.get()), float(ptB_Y.get()))
	dm = PlanoCartesiano()
	dm.calcularDistanciaManhattan(A, B)
	resultado.set(dm.getDistanciaManhattan())

# Crear la ventana principal
ventana=Tk()
# Asignar un titulo a la ventana
ventana.title('Distancia Manhattan')
#Asignar un tamaño a la ventana
ventana.geometry("640x480")
# Evitar cambiar tamaño
ventana.resizable(0,0)

# Declarar atributos de las cajas de texto

ptA_X = StringVar()
ptA_Y = StringVar()
ptB_X = StringVar()
ptB_Y = StringVar()
resultado = StringVar()

# Crear etiquetas
lbl_puntoA=Label(ventana, text="Punto A", fg='red', font=("Helvetica", 12))
lbl_puntoA.place(x=160, y=50)

lbl_puntoA_X=Label(ventana, text="X: ", fg='blue', font=("Helvetica", 10))
lbl_puntoA_X.place(x=100, y=80)

lbl_puntoA_Y=Label(ventana, text="Y: ", fg='blue', font=("Helvetica", 10))
lbl_puntoA_Y.place(x=100, y=120)

lbl_puntoB=Label(ventana, text="Punto B", fg='red', font=("Helvetica", 12))
lbl_puntoB.place(x=380, y=50)

lbl_puntoB_X=Label(ventana, text="X: ", fg='blue', font=("Helvetica", 10))
lbl_puntoB_X.place(x=320, y=80)

lbl_puntoB_Y=Label(ventana, text="Y: ", fg='blue', font=("Helvetica", 10))
lbl_puntoB_Y.place(x=320, y=120)

lbl_resultado=Label(ventana, text="Resultado: ", fg='blue', font=("Helvetica", 10))
lbl_resultado.place(x=160, y=180)

# Crear cajas de texto

txt_puntoA_X=Entry(ventana, text="Escribe un número", bd=1, textvariable=ptA_X)
txt_puntoA_X.place(x=120, y=80)

txt_puntoA_Y=Entry(ventana, text="Escribe un número", bd=1, textvariable=ptA_Y)
txt_puntoA_Y.place(x=120, y=120)

txt_puntoB_X=Entry(ventana, text="Escribe un número", bd=1, textvariable=ptB_X)
txt_puntoB_X.place(x=340, y=80)

txt_puntoB_Y=Entry(ventana, text="Escribe un número", bd=1, textvariable=ptB_Y)
txt_puntoB_Y.place(x=340, y=120)

txt_resultado=Entry(ventana, textvariable=resultado, state="disabled", bd=1)
txt_resultado.place(x=240, y=180)

btn=Button(ventana, text="Calcular", fg='blue', command=calcularDistancia)
btn.place(x=280, y=220)

# Activar ventana
ventana.mainloop()

import sqlite3
from distanciaManhattan import *

class dbDistanciaManhattan:
	__conexion = sqlite3.connect('dbDistanciaManhattan.db')

	def crearTabla(self):
		# Creamos el cursor
		cursor = self.__conexion.cursor()

		# Ahora crearemos una tabla de usuarios con nombres, edades y emails
		cursor.execute("CREATE TABLE IF NOT EXISTS dbDistanciaManhattan " \
		    "(X1 float, Y1 float, X2 float, Y2 float, distanciaManhattan float)")

		# Guardamos los cambios haciendo un commit
		self.__conexion.commit()

		
	def InsertarRegistros(self, x1, y1, x2, y2):
		# Creamos el cursor
		cursor = self.__conexion.cursor()
		A = Punto(x1, y1)
		B = Punto(x2, y2)
		dm = PlanoCartesiano()
		dm.calcularDistanciaManhattan(A, B)
		distancia = dm.getDistanciaManhattan()
		cursor.execute("INSERT INTO dbDistanciaManhattan VALUES " \
    				"(" + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2) + ", " + str(distancia) + ")")
		
		# Guardamos los cambios haciendo un commit
		self.__conexion.commit()

	def buscarRegistros(self, distanciaManhattan):
		# Creamos el cursor
		cursor = self.__conexion.cursor()
		#sql = ("SELECT * FROM dbDistanciaManhattan WHERE distanciaManhattan = " + str(distanciaManhattan))
		#print(sql)
		cursor.execute("SELECT * FROM dbDistanciaManhattan WHERE distanciaManhattan = " + str(distanciaManhattan))

		resultado = cursor.fetchall()

		for distancia in resultado:
			print(distancia)


def main():
	db = dbDistanciaManhattan()
	#db.crearTabla()
	#db.InsertarRegistros(3,6,7,8)
	#db.InsertarRegistros(7,9,15,23)
	db.buscarRegistros(8)

if __name__ == '__main__':
	main()
		
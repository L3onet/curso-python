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

		# Guardamos los cambios haciendo un commit
		self.__conexion.commit()

	def actualizarRegistro(self, A, B, C, D):
		# Creamos el cursor
		cursor = self.__conexion.cursor()

		dm = PlanoCartesiano()
		dm.calcularDistanciaManhattan(C, D)
		distancia = dm.getDistanciaManhattan()

		sql = "UPDATE dbDistanciaManhattan SET X1 = " + str(C.getX()) + " , Y1 = " + str(C.getY()) + " , X2 = " + str(D.getX()) + " , Y2 = " + str(D.getY()) + ", distanciaManhattan = " + str(distancia) + " WHERE X1 = " + str(A.getX()) + " AND Y1 = " + str(A.getY()) + " AND X2 = " + str(B.getX()) + " AND Y2 = " + str(B.getY())
		#print(sql)

		cursor.execute(sql)
		self.__conexion.commit()

	def borrarRegistro(self, A, B):
		# Creamos el cursor
		cursor = self.__conexion.cursor()

		sql = "DELETE FROM dbDistanciaManhattan WHERE X1 = " + str(A.getX()) + " AND Y1 = " + str(A.getY()) + " AND X2 = " + str(B.getX()) + " AND Y2 = " + str(B.getY())
		#print(sql)
		cursor.execute(sql)
		self.__conexion.commit()

	def cerrarConexion(self):
		self.__conexion.close()

def main():
	db = dbDistanciaManhattan()
	#db.crearTabla()
	#db.InsertarRegistros(3,6,7,8)
	#db.InsertarRegistros(7,9,15,23)
	#db.buscarRegistros(8)
	A = Punto(3,6)
	B = Punto(7,8)
	C = Punto(9,2)
	D = Punto(13,23)
	#db.actualizarRegistro(A, B, C, D)
	db.borrarRegistro(C,D)
	db.cerrarConexion()

if __name__ == '__main__':
	main()
		
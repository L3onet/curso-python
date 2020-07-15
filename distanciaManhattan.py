"""
>>> A = Punto(3.0, 6.0)
>>> B = Punto(7.0, 8.0)
>>> dm = PlanoCartesiano()
>>> dm.calcularDistanciaManhattan(A, B)
>>> dm.getDistanciaManhattan()
6.0
"""
class Punto:
	"""
	Esta clase permite crear puntos en un plano cartesiano de dos ejes: (x,y)
	"""
	__x = float(0.0)
	__y = float(0.0)

	def __init__(self, x, y):
		"""
		Método constructor para inicializar el objeto.
		Utiliza dos parámetros:
			x: un valor de tipo float
			y: un valor de tipo float
		"""
		self.__x = x
		self.__y = y

	def getX(self):
		"""
		Método GET para devolver el valor del atributo X.
		No requiere de parámetros.
		"""
		return self.__x

	def getY(self):
		"""
		Método GET para devolver el valor del atributo Y.
		No requiere de parámetros
		"""
		return self.__y


class PlanoCartesiano:
	"""
	Esta clase simula el comportamiento de un plano cartesiano.
	"""
	__distanciaManhattan = float(0.0)

	def calcularDistanciaManhattan(self, A, B):
		"""
		Este método calcula la distancia Manhatan en dos puntos en un plano cartesiano.
		Parámetros de entrada:
			A: Una instancia de la clase Punto
			B: Una instancia de la clase Punto


		Cálculo de la distancia manhattan:
			Entradas:
			A(x1, y1)
			B(x2, y2)

			Proceso:
			dm = | x2 - x1 | + | y2 - y1 |
			dm = | 7 - 3 | + | 8 - 6 |
			dm = | 4 | + | 2 |
			dm = 6
			Salida:
			dm
		"""
		self.__distanciaManhattan = (abs(B.getX() - A.getX()) + abs(B.getY() - A.getY())) 

	def getDistanciaManhattan(self):
		"""
		Este método devuelve el valor del atributo distanciaManhatan
		"""
		return self.__distanciaManhattan


"""
def main():
	A = Punto(3.0, 6.0)
	B = Punto(7.0, 8.0)
	dm = PlanoCartesiano()
	dm.calcularDistanciaManhattan(A, B)
	print(dm.getDistanciaManhattan())
"""

if __name__ == '__main__':
	#main()
	import doctest
	doctest.testmod()

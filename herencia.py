import math

class Figura:
    """
    Esta clase define la base para crear figuras geométricas.
    """
    _area = float(0)
    _perimetro = float(0)

    def calcularArea(self):
        """
        Este método crea la base para calcular el área de una figura
        """
        return 0

    def calcularPerimetro(self):
        """
        Este método crea la base para calcular el perimetro de una figura
        """
        return 0

    def getArea(self):
        """
        Este método devuelve el valor del área de la figura
        """
        return self._area

    def getPerimetro(self):
        """
        Este método devuelve el valor del perimetro de la figura
        """
        return self._perimetro


class Circulo(Figura):
    """
    Esta clase es derivada de la clase Figura. Define el comportamiento de un circulo.
    """
    __radio = float(0)

    def __init__(self, radio):
        """
        Método constructor que inicializa un objeto y le asigna el parámetro "radio".
        Parámetros utilizados:
            radio:
        """
        if (radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        """
        Este método realiza el cálculo del área de la figura geométrica Circulo.
        """
        self._area = math.pi * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        """
        Este método realiza el cálculo del perimetro de la figura geométrica Circulo.
        """
        self._perimetro = (2 * math.pi) * self.__radio


class Cuadrado(Figura):
    __lado = float(0)

    def __init__(self, lado):
        """
        Método constructor que inicializa un objeto y le asigna el parámetro "lado".
        Parámetros utilizados:
            lado:
        """
        if (lado < 0):
            self.__lado = 0
        else:
            self.__lado = lado
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        """
        Este método realiza el cálculo del área de la figura geométrica Cuadrado.
        """
        self._area = self.__lado * self.__lado

    def calcularPerimetro(self):
        """
        Este método realiza el cálculo del perimetro de la figura geométrica Cuadrado.
        """
        self._perimetro = self.__lado * 4


class Rectangulo(Figura):
    """
    Esta clase es derivada de la clase Figura. Define el comportamiento de un Rectangulo.
    """
    _base = float(0)
    _altura = float(0)

    def __init__(self, base, altura):
        """
        Método constructor que inicializa un objeto y le asigna el parámetro "lado".
        Parámetros utilizados:
            base:
            altura:
        """
        if (base < 0 or altura < 0):
            self._base = 0
            self._altura = 0
        else:
            self._base = base
            self._altura = altura
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        """
        Este método realiza el cálculo del área de la figura geométrica Rectangulo.
        """
        self._area = (self._base * self._altura)

    def calcularPerimetro(self):
        """
        Este método realiza el cálculo del perimetro de la figura geométrica Rectangulo.
        """
        self._perimetro = (self._base * 2) + (self._altura * 2)


def main():
    valor = float(input("Introduce el radio del circulo: "))
    circulo = Circulo(valor)
    print ('El área del circulo es: ', circulo.getArea())
    print ('El perimetro del circulo es: ', circulo.getPerimetro())
    valor2 = float(input("Introduce el lado del cuadrado: "))
    cuadrado = Cuadrado(valor2)
    print ('El área del cuadrado es: ', cuadrado.getArea())
    print ('El perimetro del cuadrado es: ', cuadrado.getPerimetro())

if __name__ == '__main__':
    main()
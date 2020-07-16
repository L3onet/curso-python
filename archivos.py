from distanciaManhattan import *

class Archivos:
    """
    Esta clase nos permite abrir un archivo de texto
    """
    def leerArchivo(self, archivo):
        """
        Este método abre un archivo de texto.
        Parámetros:
            archivo: nombre del archivo que se quiere abrir
        """
        file = open(archivo, 'r')       # Abrir un archivo en modo lectura (r)
        lineas = []                     # Crear una lista para guardar las líneas del archivo
        lineas_archivo = []             # Crear una lista para devolver los valores de las líneas
        for linea in file.readlines():  # Una línea termina cuando encuentra un salto de línea (\n)
            lineas.append(linea.replace('\n', '').split(',')) # Crear un arreglo de n elementos a partir de la línea del archivo
        file.close()
        #print(lineas)
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([float(lineas[f][0]), float(lineas[f][1]), float(lineas[f][2]), float(lineas[f][3])])
            except ValueError:
                lineas_archivo.append([0.0,0.0])
        #print(lineas_archivo)
        return lineas_archivo

    def realizarOperaciones(self, lista):
        """
        Realiza los cálculos de la distancia manhattan y devuelve una lista con los resultados.
        Parámetros:
            lista: puntos A y B para calcular la distancia manhattan
        """
        lista_resultados = []
        #print (lista)
        for f in range(0, len(lista)):
            #print(lista[f])
            #print(lista[f][0])
            #print(lista[f][1])
            #print(lista[f][2])
            #print(lista[f][3])
            A = Punto(lista[f][0], lista[f][1])
            B = Punto(lista[f][2], lista[f][3])
            dm = PlanoCartesiano()
            dm.calcularDistanciaManhattan(A, B)
            lista_resultados.append(dm.getDistanciaManhattan())
        return lista_resultados

    def guardarResultados(self, lista, archivo):
        """
        Guardas los resultados en un archivo de texto.
        Parámetros:
            lista: contiene los resultados
            archivo: nombre del archivo a guardar
        """
        file = open(archivo, 'w')
        file.write('distancia Manhattan\n')
        for a in range(0, len(lista)):
            linea = str(lista[a]) + '\n'
            file.write(linea)
        file.close()
        return 0


def main():
    archivo = Archivos()
    lineas = archivo.leerArchivo('puntos.txt')
    lineas2 = archivo.realizarOperaciones(lineas)
    print(lineas2)
    archivo.guardarResultados(lineas2,'resultados.txt')

if __name__==  '__main__':
   main()

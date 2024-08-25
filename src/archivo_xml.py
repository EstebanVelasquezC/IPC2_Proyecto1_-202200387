import xml.etree.ElementTree as ET
from lista_enlazada import ListaEnlazada

class Matriz:
    def __init__(self, nombre, n, m, datos):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.datos = datos  # Matriz de datos

class Archivo:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.matrices = ListaEnlazada()  # Lista enlazada para almacenar las matrices cargadas
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            tree = ET.parse(self.ruta_archivo)
            root = tree.getroot()
            print("Archivo XML cargado correctamente.")  # funciono 

            for matriz_elem in root.findall('matriz'):
                nombre = matriz_elem.get('nombre')
                n = int(matriz_elem.get('n'))
                m = int(matriz_elem.get('m'))

                if n < 1 or m < 1:
                    print(f"Error: La matriz '{nombre}' tiene dimensiones inválidas (n={n}, m={m}).")
                    continue  # Salta esta matriz si las dimensiones son inválidas

                datos = [[0]*m for _ in range(n)]

                for dato in matriz_elem.findall('dato'):
                    x = int(dato.get('x')) - 1  # Restamos 1 porque las matrices en Python son 0-indexadas
                    y = int(dato.get('y')) - 1
                    valor = int(dato.text)

                    if 0 <= x < n and 0 <= y < m:
                        datos[x][y] = valor
                    else:
                        print(f"Error: Dato fuera de los límites en la matriz '{nombre}' (x={x+1}, y={y+1}).")

                matriz = Matriz(nombre, n, m, datos)
                self.matrices.insertar_al_final(matriz)

            if self.matrices.esta_vacia():
                print("No se cargaron matrices. Verifique el archivo.")
            else:
                print("Matrices cargadas exitosamente.")  # Verificación

        except ET.ParseError as e:
            print(f"Error al parsear el archivo XML: {e}")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")


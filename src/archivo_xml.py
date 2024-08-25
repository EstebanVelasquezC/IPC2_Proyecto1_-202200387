import xml.etree.ElementTree as ET
from lista_enlazada import ListaEnlazada
from matriz import Matriz

class Archivo:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.matrices = ListaEnlazada()
        self.errores = False
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            tree = ET.parse(self.ruta_archivo)
            root = tree.getroot()
            print("Archivo XML cargado correctamente.")

            for matriz_elem in root.findall('matriz'):
                nombre = matriz_elem.get('nombre')
                n = int(matriz_elem.get('n'))
                m = int(matriz_elem.get('m'))

                if n < 1 or m < 1:
                    print(f"Error: La matriz '{nombre}' tiene dimensiones inválidas (n={n}, m={m}).")
                    self.errores = True
                    continue

                matriz = Matriz(nombre, n, m)

                for dato in matriz_elem.findall('dato'):
                    x = int(dato.get('x'))
                    y = int(dato.get('y'))
                    valor = int(dato.text)

                    try:
                        matriz.insertar_dato(x, y, valor)
                    except ValueError:
                        print(f"Error: Dato fuera de los límites en la matriz '{nombre}' (x={x}, y={y}).")
                        self.errores = True

                self.matrices.insertar_al_final(matriz)

            if self.errores:
                print("Hubo errores al cargar el archivo. No se puede procesar.")
            elif self.matrices.esta_vacia():
                print("No se cargaron matrices. Verifique el archivo.")
            else:
                print("Matrices cargadas exitosamente.")

        except ET.ParseError as e:
            print(f"Error al parsear el archivo XML: {e}")
            self.errores = True
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            self.errores = True

    def guardar_archivo_salida(self, ruta_salida):
        root = ET.Element("matrices")
        actual = self.matrices.cabeza
        while actual:
            matriz = actual.dato
            matriz_elem = ET.SubElement(
                root, 
                "matriz", 
                nombre=matriz.nombre, 
                n=str(matriz.n), 
                m=str(matriz.m)
            )
            
            nodo_dato = matriz.datos.cabeza
            while nodo_dato:
                dato = nodo_dato.dato
                if dato.valor != 0:
                    dato_elem = ET.SubElement(
                        matriz_elem, 
                        "dato", 
                        x=str(dato.x), 
                        y=str(dato.y)
                    )
                    dato_elem.text = str(dato.valor)
                nodo_dato = nodo_dato.siguiente

            actual = actual.siguiente

        tree = ET.ElementTree(root)
        tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
        print(f"Archivo de salida generado en: {ruta_salida}")

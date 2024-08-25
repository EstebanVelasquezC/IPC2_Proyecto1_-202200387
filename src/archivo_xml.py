import xml.etree.ElementTree as ET
from lista_enlazada import ListaEnlazada

class Matriz:
    def __init__(self, nombre, n, m, datos):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.datos = datos  # Matriz de datos
        self.grupos = {}  # Se almacenarán los grupos de la matriz reducida

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

                datos = [[0] * m for _ in range(n)]

                for dato in matriz_elem.findall('dato'):
                    x = int(dato.get('x')) - 1
                    y = int(dato.get('y')) - 1
                    valor = int(dato.text)

                    if 0 <= x < n and 0 <= y < m:
                        datos[x][y] = valor
                    else:
                        print(f"Error: Dato fuera de los límites en la matriz '{nombre}' (x={x+1}, y={y+1}).")
                        self.errores = True

                matriz = Matriz(nombre, n, m, datos)
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
        for matriz in self.matrices:
            matriz_elem = ET.SubElement(
                root, 
                "matriz", 
                nombre=matriz.nombre, 
                n=str(matriz.n), 
                m=str(matriz.m)
            )
            
            for i, fila in enumerate(matriz.datos):
                for j, valor in enumerate(fila):
                    if valor != 0:
                        dato_elem = ET.SubElement(
                            matriz_elem, 
                            "dato", 
                            x=str(i + 1), 
                            y=str(j + 1)
                        )
                        dato_elem.text = str(valor)

            for grupo, indices in matriz.grupos.items():
                frecuencia_elem = ET.SubElement(
                    matriz_elem, 
                    "frecuencia", 
                    g=str(grupo)
                )
                frecuencia_elem.text = str(len(indices))

        tree = ET.ElementTree(root)
        tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
        print(f"Archivo de salida generado en: {ruta_salida}")




        
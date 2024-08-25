import xml.etree.ElementTree as ET
from lista_enlazada import ListaEnlazada
from matriz import Matriz

class Archivo:
    def __init__(self, ruta_archivo):
        # Inicializa la clase con la ruta del archivo XML.
        # Crea una lista enlazada para almacenar las matrices cargadas.
        # Inicializa un flag para manejar errores.
        self.ruta_archivo = ruta_archivo
        self.matrices = ListaEnlazada()
        self.errores = False
        # Llama al método para cargar el archivo XML.
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            # Carga y analiza el archivo XML utilizando ElementTree.
            tree = ET.parse(self.ruta_archivo)
            root = tree.getroot()
            print("Archivo XML cargado correctamente.")

            # Itera sobre cada elemento de tipo 'matriz' en el archivo XML.
            for matriz_elem in root.findall('matriz'):
                # Extrae el nombre, número de filas (n) y número de columnas (m) de la matriz.
                nombre = matriz_elem.get('nombre')
                n = int(matriz_elem.get('n'))
                m = int(matriz_elem.get('m'))

                # Verifica si las dimensiones de la matriz son válidas.
                if n < 1 or m < 1:
                    print(f"Error: La matriz '{nombre}' tiene dimensiones inválidas (n={n}, m={m}).")
                    self.errores = True
                    continue

                # Crea una instancia de la matriz con el nombre y dimensiones extraídas.
                matriz = Matriz(nombre, n, m)

                # Itera sobre cada elemento de tipo 'dato' en la matriz XML.
                for dato in matriz_elem.findall('dato'):
                    # Extrae las coordenadas (x, y) y el valor del dato.
                    x = int(dato.get('x'))
                    y = int(dato.get('y'))
                    valor = int(dato.text)

                    try:
                        # Inserta el dato en la matriz en la posición correspondiente.
                        matriz.insertar_dato(x, y, valor)
                    except ValueError:
                        # Captura errores si el dato está fuera de los límites de la matriz.
                        print(f"Error: Dato fuera de los límites en la matriz '{nombre}' (x={x}, y={y}).")
                        self.errores = True

                # Inserta la matriz en la lista de matrices.
                self.matrices.insertar_al_final(matriz)

            # Verifica si ocurrieron errores o si no se cargaron matrices.
            if self.errores:
                print("Hubo errores al cargar el archivo. No se puede procesar.")
            elif self.matrices.esta_vacia():
                print("No se cargaron matrices. Verifique el archivo.")
            else:
                print("Matrices cargadas exitosamente.")

        except ET.ParseError as e:
            # Captura errores de análisis del archivo XML.
            print(f"Error al parsear el archivo XML: {e}")
            self.errores = True
        except Exception as e:
            # Captura otros errores generales.
            print(f"Error al cargar el archivo: {e}")
            self.errores = True

    def guardar_archivo_salida(self, ruta_salida):
        # Crea un elemento raíz para el archivo XML de salida.
        root = ET.Element("matrices")
        actual = self.matrices.cabeza
        
        # Itera sobre cada matriz en la lista de matrices.
        while actual:
            matriz = actual.dato
            matriz_elem = ET.SubElement(
                root, 
                "matriz", 
                nombre=matriz.nombre, 
                n=str(matriz.n), 
                m=str(matriz.m)
            )
            
            # Itera sobre los datos de la matriz.
            nodo_dato = matriz.datos.cabeza
            while nodo_dato:
                dato = nodo_dato.dato
                # Solo agrega datos con valores distintos de cero.
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

        # Crea un árbol XML y escribe el archivo de salida.
        tree = ET.ElementTree(root)
        tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
        print(f"Archivo de salida generado en: {ruta_salida}")

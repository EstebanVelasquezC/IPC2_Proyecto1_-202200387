import os
import xml.etree.ElementTree as ET
from graphviz import Digraph

class Azulejo:
    def __init__(self, color='blanco'):
        self.color = color

    def voltear(self):
        self.color = 'negro' if self.color == 'blanco' else 'blanco'

class Piso:
    def __init__(self, nombre, filas, columnas, costo_volteo, costo_intercambio):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.costo_volteo = costo_volteo
        self.costo_intercambio = costo_intercambio
        self.matriz = [[Azulejo() for _ in range(columnas)] for _ in range(filas)]

    def mostrar_piso(self):
        for fila in self.matriz:
            for azulejo in fila:
                print(azulejo.color[0], end=' ')
            print()

    def mostrar_graficamente(self):
        dot = Digraph(comment=f'Patron del Piso {self.nombre}')
        node_size = 0.5 
        node_margin = 0.01  
        node_sep = 0  

        dot.attr(nodesep=str(node_sep))

        for i in range(self.filas):
            for j in range(self.columnas):
                color_nodo = 'black' if (i + j) % 2 == 0 else 'white'
                dot.node(f'{i * self.columnas + j}', shape='rect', width=str(node_size), height=str(node_size), style='filled', fillcolor=color_nodo, margin=str(node_margin))

        for i in range(self.filas - 1):
            for j in range(self.columnas):
                dot.edge(f'{i * self.columnas + j}', f'{(i + 1) * self.columnas + j}')

        dot.render(f'patron_piso_{self.nombre}', format='png', cleanup=True)

    def cambiar_patron(self, nuevo_codigo):
        costo_total = 0
        instrucciones = []

        if len(nuevo_codigo) != self.filas * self.columnas:
            print("Error: Longitud incorrecta del codigo de patron.")
            return

        for i in range(self.filas):
            for j in range(self.columnas):
                azulejo_actual = self.matriz[i][j]
                azulejo_objetivo = nuevo_codigo[i * self.columnas + j]

                if azulejo_actual.color != azulejo_objetivo:
                    costo_total += self.costo_volteo
                    instrucciones.append(f"Voltear azulejo en posicion ({i+1}, {j+1})")

        print(f"Costo minimo para cambiar el patron: {costo_total} Quetzales")
        print("Instrucciones:")
        for instruccion in instrucciones:
            print(instruccion)

        self.mostrar_graficamente()

def cargar_xml(nombre_archivo):
    while not os.path.exists(nombre_archivo):
        print(f"Error: No se encontro el archivo en la ruta {nombre_archivo}")
        nombre_archivo = input("Ingrese una ruta valida para el archivo XML: ")

    try:
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

        pisos = []
        for piso_xml in root.findall('piso'):
            nombre_piso = piso_xml.get('nombre')
            filas_piso = int(piso_xml.find('R').text)
            columnas_piso = int(piso_xml.find('C').text)
            costo_volteo_piso = int(piso_xml.find('F').text)
            costo_intercambio_piso = int(piso_xml.find('S').text)
            piso_nuevo = Piso(nombre_piso, filas_piso, columnas_piso, costo_volteo_piso, costo_intercambio_piso)

            for patron_xml in piso_xml.find('patrones').findall('patron'):
                codigo_patron = patron_xml.text.strip()
                codigo_patron = codigo_patron.ljust(piso_nuevo.filas * piso_nuevo.columnas, 'B')
                codigo_patron = codigo_patron[:piso_nuevo.filas * piso_nuevo.columnas]
                piso_nuevo.cambiar_patron(codigo_patron)

            pisos.append(piso_nuevo)

        return pisos
    except ET.ParseError as e:
        print(f"Error al cargar el archivo XML: {e}")
        print(f"Posiblemente hay un problema en la linea {e.position[0]}, columna {e.position[1]} del archivo XML.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar el archivo XML: {e}")
        return []

def main():
    nombre_estudiante = "Rogelio Esteban Velasquez Castillo"
    carnet_estudiante = "202200387"
    curso_estudiante = "IPC2"

    print(f"Informacion del estudiante:\nNombre: {nombre_estudiante}\nCarnet: {carnet_estudiante}\nCurso: {curso_estudiante}\n")

    archivo_xml = input("Ingrese el nombre del archivo XML: ")
    pisos_cargados = cargar_xml(archivo_xml)
    if pisos_cargados:
        print("\nPisos cargados exitosamente.")
        for piso in pisos_cargados:
            print(f"\nMostrando informacion del piso: {piso.nombre}")
            piso.mostrar_piso()
            print("\nMostrando graficamente el patron del piso:")
            piso.mostrar_graficamente()

if __name__ == "__main__":
    main()

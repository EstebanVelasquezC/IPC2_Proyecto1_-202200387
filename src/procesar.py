from lista_enlazada import ListaEnlazada, Nodo
from matriz import Matriz, DatoMatriz

class Procesador:
    def __init__(self, matrices):
        # Inicializa la clase con una lista de matrices.
        self.matrices = matrices

    def obtener_patrones_acceso(self, matriz):
        # Crea una lista enlazada para almacenar los patrones de acceso.
        patrones = ListaEnlazada()
        
        # Itera sobre cada fila de la matriz.
        for i in range(1, matriz.n + 1):
            patron = ''
            # Itera sobre cada columna de la fila actual.
            for j in range(1, matriz.m + 1):
                # Obtiene el valor del dato en la posición (i, j).
                valor = matriz.obtener_dato(i, j)
                # Construye un patrón binario donde '1' indica un valor positivo y '0' indica un valor cero.
                patron += '1' if valor > 0 else '0'
            # Inserta el patrón en la lista enlazada.
            patrones.insertar_al_final(patron)
        
        # Retorna la lista enlazada de patrones.
        return patrones

    def agrupar_patrones(self, patrones):
        # Crea dos listas enlazadas: una para almacenar patrones únicos y otra para los grupos de patrones.
        patrones_unicos = ListaEnlazada()
        grupos = ListaEnlazada()
        
        # Obtiene el primer nodo de la lista de patrones.
        actual = patrones.cabeza
        
        # Recorre todos los patrones en la lista.
        while actual:
            patron = actual.dato
            
            # Verifica si el patrón ya está en la lista de patrones únicos.
            if not self._encontrar_patron(patron, patrones_unicos):
                # Crea una lista enlazada para almacenar los índices de las filas con el patrón actual.
                grupo = ListaEnlazada()
                indice = 1
                actual_patron = patrones.cabeza
                
                # Recorre todos los patrones para encontrar las filas que coinciden con el patrón actual.
                while actual_patron:
                    if actual_patron.dato == patron:
                        # Inserta el índice de la fila en el grupo.
                        grupo.insertar_al_final(indice)
                    indice += 1
                    actual_patron = actual_patron.siguiente
                
                # Inserta el patrón único en la lista de patrones únicos.
                patrones_unicos.insertar_al_final(patron)
                # Inserta el patrón y su grupo de índices en la lista de grupos.
                grupos.insertar_al_final((patron, grupo))
            
            actual = actual.siguiente
        
        # Retorna la lista enlazada de grupos de patrones.
        return grupos

    def _encontrar_patron(self, patron, lista):
        # Busca un patrón en una lista enlazada.
        actual = lista.cabeza
        while actual:
            if actual.dato == patron:
                return True
            actual = actual.siguiente
        return False

    def generar_matriz_reducida(self, matriz, grupos):
        # Crea una lista enlazada para almacenar la matriz reducida.
        matriz_reducida = ListaEnlazada()
        
        # Recorre cada grupo de patrones.
        actual = grupos.cabeza
        while actual:
            patron, indices = actual.dato
            nueva_fila = ListaEnlazada()
            
            # Itera sobre cada columna de la matriz.
            for j in range(1, matriz.m + 1):
                suma_columna = 0
                indice_nodo = indices.cabeza
                
                # Suma los valores de las filas que tienen el mismo patrón para la columna actual.
                while indice_nodo:
                    indice = indice_nodo.dato
                    suma_columna += matriz.obtener_dato(indice, j)
                    indice_nodo = indice_nodo.siguiente
                
                # Inserta la suma de la columna en la nueva fila.
                nueva_fila.insertar_al_final(suma_columna)
            
            # Inserta la nueva fila en la matriz reducida.
            matriz_reducida.insertar_al_final(nueva_fila)
            actual = actual.siguiente
        
        # Retorna la matriz reducida.
        return matriz_reducida

    def procesar_matriz(self, matriz):
        # Obtiene los patrones de acceso de la matriz.
        patrones = self.obtener_patrones_acceso(matriz)
        # Agrupa los patrones en función de su frecuencia.
        grupos = self.agrupar_patrones(patrones)
        # Genera la matriz reducida usando los grupos de patrones.
        matriz_reducida = self.generar_matriz_reducida(matriz, grupos)
        # Retorna la matriz reducida y los grupos de patrones.
        return matriz_reducida, grupos

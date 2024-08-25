from lista_enlazada import ListaEnlazada, Nodo
from matriz import Matriz, DatoMatriz

class Procesador:
    def __init__(self, matrices):
        self.matrices = matrices

    def obtener_patrones_acceso(self, matriz):
        patrones = ListaEnlazada()
        for i in range(1, matriz.n + 1):
            patron = ''
            for j in range(1, matriz.m + 1):
                valor = matriz.obtener_dato(i, j)
                patron += '1' if valor > 0 else '0'
            patrones.insertar_al_final(patron)
        return patrones

    def agrupar_patrones(self, patrones):
        patrones_unicos = ListaEnlazada()
        grupos = ListaEnlazada()
        actual = patrones.cabeza
        while actual:
            patron = actual.dato
            if not self._encontrar_patron(patron, patrones_unicos):
                grupo = ListaEnlazada()
                indice = 1
                actual_patron = patrones.cabeza
                while actual_patron:
                    if actual_patron.dato == patron:
                        grupo.insertar_al_final(indice)
                    indice += 1
                    actual_patron = actual_patron.siguiente
                patrones_unicos.insertar_al_final(patron)
                grupos.insertar_al_final((patron, grupo))  # Usamos una tupla para almacenar patron y grupo
            actual = actual.siguiente
        return grupos

    def _encontrar_patron(self, patron, lista):
        actual = lista.cabeza
        while actual:
            if actual.dato == patron:
                return True
            actual = actual.siguiente
        return False

    def generar_matriz_reducida(self, matriz, grupos):
        matriz_reducida = ListaEnlazada()
        actual = grupos.cabeza
        while actual:
            patron, indices = actual.dato
            nueva_fila = ListaEnlazada()
            for j in range(1, matriz.m + 1):
                suma_columna = 0
                indice_nodo = indices.cabeza
                while indice_nodo:
                    indice = indice_nodo.dato
                    suma_columna += matriz.obtener_dato(indice, j)
                    indice_nodo = indice_nodo.siguiente
                nueva_fila.insertar_al_final(suma_columna)
            matriz_reducida.insertar_al_final(nueva_fila)
            actual = actual.siguiente
        return matriz_reducida

    def procesar_matriz(self, matriz):
        patrones = self.obtener_patrones_acceso(matriz)
        grupos = self.agrupar_patrones(patrones)
        matriz_reducida = self.generar_matriz_reducida(matriz, grupos)
        return matriz_reducida, grupos
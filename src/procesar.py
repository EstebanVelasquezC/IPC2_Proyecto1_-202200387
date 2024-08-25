from lista_enlazada import ListaEnlazada

class Procesador:
    def __init__(self, matrices):
        self.matrices = matrices

    def obtener_patrones_acceso(self, matriz):
        patrones = []
        for fila in matriz:
            patron = ''.join(['1' if x > 0 else '0' for x in fila])
            patrones.append(patron)
        return patrones

    def agrupar_patrones(self, patrones):
        grupos = {}
        for i, patron in enumerate(patrones):
            if patron in grupos:
                grupos[patron].append(i)
            else:
                grupos[patron] = [i]
        return grupos
   #Nomas quiero dormir :(
    def generar_matriz_reducida(self, matriz, grupos):
        matriz_reducida = []
        for indices in grupos.values():
            nueva_fila = [0] * len(matriz[0])
            for indice in indices:
                for j in range(len(matriz[indice])):
                    nueva_fila[j] += matriz[indice][j]
            matriz_reducida.append(nueva_fila)
        return matriz_reducida

    def procesar_matriz(self, matriz):
        patrones = self.obtener_patrones_acceso(matriz)
        grupos = self.agrupar_patrones(patrones)
        matriz_reducida = self.generar_matriz_reducida(matriz, grupos)
        return matriz_reducida, grupos

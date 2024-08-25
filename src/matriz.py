from lista_enlazada import ListaEnlazada

class DatoMatriz:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre  # Nombre de la matriz
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.datos = ListaEnlazada()  # Lista enlazada para almacenar los datos de la matriz

    def insertar_dato(self, x, y, valor):
        if 1 <= x <= self.n and 1 <= y <= self.m:
            nuevo_dato = DatoMatriz(x, y, valor)
            self.datos.insertar_al_final(nuevo_dato)
        else:
            raise ValueError("Coordenadas fuera del rango permitido")

    def obtener_dato(self, x, y):
        actual = self.datos.cabeza
        while actual:
            if actual.dato.x == x and actual.dato.y == y:
                return actual.dato.valor
            actual = actual.siguiente
        return 0  # Retornar 0 si el dato no se encuentra

    def mostrar(self):
        for i in range(1, self.n + 1):
            fila = ""
            for j in range(1, self.m + 1):
                valor = self.obtener_dato(i, j)
                fila += str(valor) + " "
            print(fila.strip())

    def obtener_fila(self, numero_fila):
        """Devuelve una lista enlazada con los datos de la fila especificada."""
        fila = ListaEnlazada()
        for j in range(1, self.m + 1):
            valor = self.obtener_dato(numero_fila, j)
            fila.insertar_al_final(valor)
        return fila
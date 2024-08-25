from lista_enlazada import ListaEnlazada

class DatoMatriz:
    def __init__(self, x, y, valor):
        # Inicializa un dato de matriz con las coordenadas (x, y) y el valor asociado.
        self.x = x      # Fila de la matriz donde se encuentra el dato.
        self.y = y      # Columna de la matriz donde se encuentra el dato.
        self.valor = valor  # Valor del dato en la matriz.

class Matriz:
    def __init__(self, nombre, n, m):
        # Inicializa una matriz con un nombre, un número de filas (n) y columnas (m).
        self.nombre = nombre  # Nombre de la matriz.
        self.n = n            # Número de filas en la matriz.
        self.m = m            # Número de columnas en la matriz.
        self.datos = ListaEnlazada()  # Lista enlazada para almacenar los datos de la matriz.

    def insertar_dato(self, x, y, valor):
        # Inserta un dato en la matriz en las coordenadas (x, y) con el valor dado.
        if 1 <= x <= self.n and 1 <= y <= self.m:
            # Verifica si las coordenadas están dentro del rango permitido de la matriz.
            nuevo_dato = DatoMatriz(x, y, valor)  # Crea un nuevo objeto DatoMatriz.
            self.datos.insertar_al_final(nuevo_dato)  # Inserta el dato en la lista enlazada.
        else:
            # Si las coordenadas están fuera del rango, lanza una excepción.
            raise ValueError("Coordenadas fuera del rango permitido")

    def obtener_dato(self, x, y):
        # Obtiene el valor del dato en las coordenadas (x, y) de la matriz.
        actual = self.datos.cabeza
        while actual:
            # Recorre la lista enlazada buscando el dato con las coordenadas especificadas.
            if actual.dato.x == x and actual.dato.y == y:
                return actual.dato.valor  # Retorna el valor del dato si se encuentra.
            actual = actual.siguiente
        return 0  # Retorna 0 si el dato no se encuentra en las coordenadas especificadas.

    def mostrar(self):
        # Muestra la matriz en formato de texto.
        for i in range(1, self.n + 1):
            fila = ""
            for j in range(1, self.m + 1):
                valor = self.obtener_dato(i, j)  # Obtiene el valor del dato en la posición (i, j).
                fila += str(valor) + " " 
            print(fila.strip())  # Imprime la fila, eliminando espacios en blanco al final.

    def obtener_fila(self, numero_fila):
        """Devuelve una lista enlazada con los datos de la fila especificada."""
        fila = ListaEnlazada()  # Crea una nueva lista enlazada para almacenar los datos de la fila.
        for j in range(1, self.m + 1):
            valor = self.obtener_dato(numero_fila, j)  # Obtiene el valor del dato en la fila especificada
            fila.insertar_al_final(valor)  # Inserta el valor en la lista enlazada.
        return fila  # Retorna la lista enlazada que contiene los datos de la fila.

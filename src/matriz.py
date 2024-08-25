from lista_enlazada import ListaEnlazada

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre  # Nombre  matriz
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.datos = ListaEnlazada()  # Lista enlazada para almacenar los datos de la matriz

    def insertar_dato(self, x, y, valor):
        if 1 <= x <= self.n and 1 <= y <= self.m:
            self.datos.insertar_al_final((x, y, valor))
        else:
            raise ValueError("Coordenadas fuera del rango permitido")

    def obtener_dato(self, x, y):
        actual = self.datos.cabeza
        while actual:
            if actual.dato[0] == x and actual.dato[1] == y:
                return actual.dato[2]
            actual = actual.siguiente
        return None  # Si no se encuentra el dato, se retorna None

    def mostrar(self):
      actual = self.datos.cabeza
      for i in range(1, self.n + 1):
        fila = []
        for j in range(1, self.m + 1):
            valor = self.obtener_dato(i, j)
            if valor is None:
                fila.append('0')
            else:
                fila.append(str(valor))
        print(" ".join(fila))

#Nomas prueba 
# if __name__ == "__main__":
#     matriz = Matriz("Ejemplo", 4, 4)
#     matriz.insertar_dato(1, 1, 2)
#     matriz.insertar_dato(1, 2, 3)
#     matriz.insertar_dato(1, 4, 4)
#     matriz.insertar_dato(2, 3, 6)
#     matriz.insertar_dato(3, 1, 3)
#     matriz.insertar_dato(4, 4, 5)
#     matriz.mostrar()


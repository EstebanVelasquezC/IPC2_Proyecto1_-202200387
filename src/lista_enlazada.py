class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Referencia al siguiente nodo 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La cabeza de lista

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return  # El dato no se encontró
        if anterior is None:
            self.cabeza = actual.siguiente  # El dato está en la cabeza
        else:
            anterior.siguiente = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
# Prueba 
# if __name__ == "__main__":
#     lista = ListaEnlazada()
#     lista.insertar_al_final(1)
#     lista.insertar_al_final(2)
#     lista.insertar_al_final(3)
#     lista.mostrar()  # Debería mostrar: 1 -> 2 -> 3 -> None

#     lista.insertar_al_inicio(0)
#     lista.mostrar()  # Debería mostrar: 0 -> 1 -> 2 -> 3 -> None

#     lista.eliminar(2)
#     lista.mostrar()  # Debería mostrar: 0 -> 1 -> 3 -> None

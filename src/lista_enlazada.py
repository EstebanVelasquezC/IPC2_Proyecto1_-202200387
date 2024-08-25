class Nodo:
    def __init__(self, dato):
        # Inicializa un nodo con un dato y un puntero al siguiente nodo.
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        # Inicializa una lista enlazada con la cabeza en None (vacía).
        self.cabeza = None

    def esta_vacia(self):
        # Verifica si la lista está vacía.
        # Retorna True si la cabeza es None, indicando que no hay nodos en la lista.
        return self.cabeza is None

    def insertar_al_final(self, dato):
        # Inserta un nuevo nodo al final de la lista con el dato proporcionado.
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato.
        if self.esta_vacia():
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza.
            self.cabeza = nuevo_nodo
        else:
            # Si la lista no está vacía, recorre hasta el último nodo y agrega el nuevo nodo.
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def insertar_al_inicio(self, dato):
        # Inserta un nuevo nodo al inicio de la lista con el dato proporcionado.
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato.
        nuevo_nodo.siguiente = self.cabeza  # Apunta el siguiente del nuevo nodo al nodo actual de la cabeza.
        self.cabeza = nuevo_nodo  # Actualiza la cabeza para que apunte al nuevo nodo.

    def eliminar(self, dato):
        # Elimina el primer nodo que contiene el dato especificado.
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            # Si el nodo con el dato no se encuentra, no se hace nada.
            return
        if anterior is None:
            # Si el nodo a eliminar es la cabeza, actualiza la cabeza para el siguiente nodo.
            self.cabeza = actual.siguiente
        else:
            # Si el nodo a eliminar no es la cabeza, el nodo anterior apunta al siguiente nodo.
            anterior.siguiente = actual.siguiente

    def mostrar(self):
        # Imprime todos los datos en la lista, desde la cabeza hasta el final.
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def __iter__(self):
        # Permite la iteración sobre la lista utilizando un bucle for.
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def contar_elementos(self):
        # Cuenta el número de nodos en la lista.
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

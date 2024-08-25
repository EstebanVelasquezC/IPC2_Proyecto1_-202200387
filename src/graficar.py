from graphviz import Digraph
from matriz import Matriz

def graficar_matriz(matriz: Matriz, nombre_matriz: str):
    dot = Digraph(comment=f'Matriz {nombre_matriz}')

    # Nodo raíz para "Matrices"
    dot.node('matrices', 'Matrices', shape='ellipse', style='filled', fillcolor='lightgrey')
    
    # Nodo para el nombre de la matriz
    dot.node('ejemplo', nombre_matriz, shape='ellipse', style='filled', fillcolor='white')

    # Conectar "Matrices" con el nombre de la matriz
    dot.edge('matrices', 'ejemplo')

    # Nodos para n y m (dimensiones)
    dot.node('nodo_n', f'n = {matriz.n}', shape='circle', color='blue', style='filled', fillcolor='lightblue')
    dot.node('nodo_m', f'm = {matriz.m}', shape='circle', color='blue', style='filled', fillcolor='lightblue')

    # Conectar "Ejemplo" con n y m
    dot.edge('ejemplo', 'nodo_n', label='n')
    dot.edge('ejemplo', 'nodo_m', label='m')

    # Nodos para cada elemento de la matriz
    for i in range(1, matriz.n + 1):
        for j in range(1, matriz.m + 1):
            valor = matriz.obtener_dato(i, j)
            dot.node(f'{i}_{j}', str(valor), shape='box', style='filled', fillcolor='lightyellow')

    # Conectar los nodos de la matriz verticalmente (entre columnas)
    for j in range(1, matriz.m + 1):
        for i in range(1, matriz.n + 1):
            if i < matriz.n:
                dot.edge(f'{i}_{j}', f'{i+1}_{j}', style='dashed')  # Conectar hacia abajo

    # Guardar el gráfico en formato PNG con el nombre de la matriz
    nombre_archivo = f'{nombre_matriz}.png'
    dot.render(filename=nombre_archivo, format='png', cleanup=True)
    print(f'Gráfico generado: {nombre_archivo}')

def graficar_matriz_reducida(matriz_reducida, nombre_matriz: str):
    dot = Digraph(comment=f'Matriz Reducida {nombre_matriz}')

    # Nodo raíz para "Matrices Reducidas"
    dot.node('matrices_reducidas', 'Matrices Reducidas', shape='ellipse', style='filled', fillcolor='lightgrey')

    # Iterar sobre las filas de la matriz reducida
    fila_actual = matriz_reducida.cabeza
    i = 1
    while fila_actual:
        fila = fila_actual.dato
        valor_actual = fila.cabeza
        j = 1
        while valor_actual:
            valor = valor_actual.dato
            dot.node(f'{i}_{j}', str(valor), shape='box', style='filled', fillcolor='lightyellow')

            # Conectar verticalmente
            if i > 1:
                dot.edge(f'{i-1}_{j}', f'{i}_{j}', style='dashed')

            valor_actual = valor_actual.siguiente
            j += 1

        fila_actual = fila_actual.siguiente
        i += 1

    # Guardar el gráfico en formato PNG con el nombre de la matriz reducida
    nombre_archivo = f'{nombre_matriz}_reducida.png'
    dot.render(filename=nombre_archivo, format='png', cleanup=True)
    print(f'Gráfico de matriz reducida generado: {nombre_archivo}')

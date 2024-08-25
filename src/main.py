from archivo_xml import Archivo
from procesar import Procesador
from graficar import graficar_matriz, graficar_matriz_reducida
import os
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def mostrar_menu():
    print("Menú principal:")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salida")

def cargar_archivo():
    ruta = input("Ingrese la ruta del archivo: ")
    archivo = Archivo(ruta)
    if archivo.errores:
        print("No se cargaron matrices debido a errores en el archivo.")
    elif archivo.matrices.esta_vacia():
        print("No se cargaron matrices. Verifique el archivo.")
    else:
        print("Archivo cargado y matrices almacenadas en memoria.")
    return archivo

def procesar_archivo(archivo):
    if archivo.errores:
        print("No se puede procesar el archivo debido a errores en la carga.")
        return

    procesador = Procesador(archivo.matrices)  # Se pasa la lista enlazada de matrices
    actual_matriz = archivo.matrices.cabeza
    while actual_matriz:
        matriz = actual_matriz.dato
        print(f"Procesando matriz '{matriz.nombre}'...")
        matriz_reducida, grupos = procesador.procesar_matriz(matriz)
        matriz.matriz_reducida = matriz_reducida
        matriz.grupos = grupos
        print("Matriz procesada:")
        actual_fila = matriz_reducida.cabeza
        while actual_fila:
            fila = actual_fila.dato
            fila_str = ' '.join(map(str, fila))
            print(fila_str)
            actual_fila = actual_fila.siguiente
        actual_matriz = actual_matriz.siguiente

def escribir_archivo_salida(archivo):
    if archivo.errores:
        print("No se puede generar el archivo de salida debido a errores en la carga.")
        return
    
    nombre_archivo = os.path.splitext(os.path.basename(archivo.ruta_archivo))[0]
    ruta_salida = f"{nombre_archivo}_salida.xml"

    root = ET.Element("matrices")

    actual_matriz = archivo.matrices.cabeza
    while actual_matriz:
        matriz = actual_matriz.dato
        matriz_elem = ET.SubElement(root, "matriz", nombre=matriz.nombre, n=str(matriz.n), m=str(matriz.m), g=str(matriz.grupos.contar_elementos()))
        
        fila_actual = matriz.matriz_reducida.cabeza
        i = 1
        while fila_actual:
            fila = fila_actual.dato
            
            # Itera sobre los elementos de la fila ( lista enlazada)
            j = 1
            valor_actual = fila.cabeza
            while valor_actual:
                valor = valor_actual.dato
                if valor != 0:
                    dato_elem = ET.SubElement(matriz_elem, "dato", x=str(i), y=str(j))
                    dato_elem.text = str(valor)
                valor_actual = valor_actual.siguiente
                j += 1

            fila_actual = fila_actual.siguiente
            i += 1
        
        grupo_actual = matriz.grupos.cabeza
        while grupo_actual:
            patron, indices = grupo_actual.dato
            frecuencia_elem = ET.SubElement(matriz_elem, "frecuencia", g=patron)
            frecuencia_elem.text = str(indices.contar_elementos())  # Se cuenta el número de elementos en `indices`
            grupo_actual = grupo_actual.siguiente
        
        actual_matriz = actual_matriz.siguiente
    
    indent(root)
    
    tree = ET.ElementTree(root)
    tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
    print(f"Archivo de salida generado en: {ruta_salida}")

def seleccionar_matriz(archivo):
    if archivo.matrices.esta_vacia():
        print("No hay matrices disponibles.")
        return None
    actual = archivo.matrices.cabeza
    index = 1
    while actual:
        print(f"{index}. {actual.dato.nombre}")
        actual = actual.siguiente
        index += 1

    seleccion = int(input("Seleccione el número de la matriz: "))
    actual = archivo.matrices.cabeza
    for _ in range(seleccion - 1):
        actual = actual.siguiente
    return actual.dato

def main():
    archivo = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            archivo = cargar_archivo()
        elif opcion == "2":
            if archivo:
                procesar_archivo(archivo)
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "3":
            if archivo:
                escribir_archivo_salida(archivo)
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "4":
            print("Carné: 202200387")
            print("Nombre: Rogelio Esteban Velasquez Castillo")
            print("Curso: IPC2")
            print("Carrera: Ingeniería en Sistemas")
            print("Semestre: cuarto")
            print("Documentación: https://drive.google.com/drive/folders/1CvEbjMaMW1oQdZzTf3cP9EW1cEjLfu-I?usp=sharing")
        elif opcion == "5":
            if archivo:
                matriz_seleccionada = seleccionar_matriz(archivo)
                if matriz_seleccionada:
                    matriz_reducida = matriz_seleccionada.matriz_reducida
                    
                    print("Generando gráfica para la matriz seleccionada...")
                    graficar_matriz(matriz_seleccionada, 'matriz_seleccionada')
                    
                    print("Generando gráfica para la matriz reducida...")
                    graficar_matriz_reducida(matriz_reducida, 'matriz_reducida')
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


 #C:\io\S IPC\ipc2\IPC2_Proyecto1_-202200387\p1_ejemplo_entrada.xml
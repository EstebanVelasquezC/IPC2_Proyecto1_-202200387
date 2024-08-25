from archivo_xml import Archivo
from procesar import Procesador
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

    for matriz in archivo.matrices:
        print(f"Procesando matriz '{matriz.nombre}'...")
        procesador = Procesador(matriz.datos)
        matriz_reducida, grupos = procesador.procesar_matriz(matriz.datos)
        matriz.matriz_reducida = matriz_reducida
        matriz.grupos = grupos
        print("Matriz procesada:")
        for fila in matriz_reducida:
            print(fila)

def escribir_archivo_salida(archivo):
    if archivo.errores:
        print("No se puede generar el archivo de salida debido a errores en la carga.")
        return
    
    nombre_archivo = os.path.splitext(os.path.basename(archivo.ruta_archivo))[0]
    ruta_salida = f"{nombre_archivo}_salida.xml"

    root = ET.Element("matrices")

    for matriz in archivo.matrices:
        matriz_elem = ET.SubElement(root, "matriz", nombre=matriz.nombre, n=str(matriz.n), m=str(matriz.m), g=str(len(matriz.grupos)))
        
        for i, fila in enumerate(matriz.matriz_reducida):
            for j, valor in enumerate(fila):
                if valor != 0:
                    dato_elem = ET.SubElement(matriz_elem, "dato", x=str(i+1), y=str(j+1))
                    dato_elem.text = str(valor)
        
        for grupo, indices in matriz.grupos.items():
            frecuencia_elem = ET.SubElement(matriz_elem, "frecuencia", g=grupo)
            frecuencia_elem.text = str(len(indices))
    
    indent(root)
    
    tree = ET.ElementTree(root)
    tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
    print(f"Archivo de salida generado en: {ruta_salida}")

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
            print("Documentación: PENDIENTE")
        elif opcion == "5":
            if archivo:
                print("Generando gráfica...")
                # Código para generar gráfica
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


           #C:\io\S IPC\ipc2\IPC2_Proyecto1_-202200387\entrada.xml 
           #C:\io\S IPC\ipc2\IPC2_Proyecto1_-202200387\p1_ejemplo_entrada.xml


     
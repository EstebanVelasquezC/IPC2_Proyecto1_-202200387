
from archivo_xml import Archivo

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
    if archivo.matrices.esta_vacia():
        print("No se cargaron matrices. Verifique el archivo.")
    else:
        print("Archivo cargado y matrices almacenadas en memoria.")
    return archivo

def main():
    archivo = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            archivo = cargar_archivo()
        elif opcion == "2":
            if archivo:
                print("Procesando archivo...")
                # proceso 
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "3":
            if archivo:
                print("Escribiendo archivo de salida...")
                # el de salida 
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
                print("que no se me olvide pa")
              
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
              
            
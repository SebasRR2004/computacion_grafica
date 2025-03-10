import numpy as np

# 1. Crear un Array Unidimensional
def crear_array_unidimensional():
    array = np.arange(1, 11)
    print("Array unidimensional:", array)

# 2. Crear un Array Multidimensional
def crear_array_multidimensional():
    matriz = np.arange(1, 10).reshape(3, 3)
    print("Matriz 2D:\n", matriz)

# 3. Operaciones Básicas con Arrays
def operaciones_basicas_con_arrays():
    array1 = np.arange(1, 6)
    array2 = np.arange(1, 6)
    suma = array1 + array2
    print("Suma de arrays:", suma)

# 4. Funciones Matemáticas
def funciones_matematicas():
    array = np.arange(1, 6)
    exponencial = np.exp(array)
    print("Exponencial de cada elemento:", exponencial)

# 5. Indexación y Segmentación
def indexacion_y_segmentacion():
    array = np.arange(1, 11)
    elementos_pares = array[array % 2 == 0]
    print("Elementos pares:", elementos_pares)

# 6. Generación de Datos Aleatorios
def generacion_de_datos_aleatorios():
    array_aleatorio = np.random.rand(10)
    print("Array de números aleatorios:", array_aleatorio)

# 7. Funciones de Agregación
def funciones_de_agregacion():
    array = np.arange(1, 6)
    media = np.mean(array)
    print("Media de los elementos:", media)

# 8. Creación de Arrays con Funciones de Fábrica
def creacion_de_arrays_con_funciones_de_fabrica():
    array = np.full(5, 7)
    print("Array con valor 7:", array)

# 9. Operaciones de Alineación y Broadcasting
def operaciones_de_alineacion_y_broadcasting():
    array1 = np.arange(1, 4)
    array2 = np.arange(4, 7)
    suma = array1 + array2
    print("Suma con broadcasting:", suma)

# 10. Funciones de Transformación y Redimensionamiento
def funciones_de_transformacion_y_redimensionamiento():
    array = np.arange(1, 7)
    matriz = array.reshape(2, 3)
    print("Matriz 2x3:\n", matriz)

# Función que muestra el Menú de opciones con las funciones anteriores
def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Crear un Array Unidimensional")
        print("2. Crear un Array Multidimensional")
        print("3. Operaciones Básicas con Arrays")
        print("4. Funciones Matemáticas")
        print("5. Indexación y Segmentación")
        print("6. Generación de Datos Aleatorios")
        print("7. Funciones de Agregación")
        print("8. Creación de Arrays con Funciones de Fábrica")
        print("9. Operaciones de Alineación y Broadcasting")
        print("10. Funciones de Transformación y Redimensionamiento")
        print("11. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            crear_array_unidimensional()
        elif opcion == 2:
            crear_array_multidimensional()
        elif opcion == 3:
            operaciones_basicas_con_arrays()
        elif opcion == 4:
            funciones_matematicas()
        elif opcion == 5:
            indexacion_y_segmentacion()
        elif opcion == 6:
            generacion_de_datos_aleatorios()
        elif opcion == 7:
            funciones_de_agregacion()
        elif opcion == 8:
            creacion_de_arrays_con_funciones_de_fabrica()
        elif opcion == 9:
            operaciones_de_alineacion_y_broadcasting()
        elif opcion == 10:
            funciones_de_transformacion_y_redimensionamiento()
        elif opcion == 11:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
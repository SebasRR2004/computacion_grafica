import random
import string
import re

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero"

def calculadora():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    operaciones = {'+': suma, '-': resta, '*': multiplicacion, '/': division}
    resultado = operaciones.get(operacion, lambda x, y: "Operación no válida")(a, b)
    print("Resultado:", resultado)

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

def convertir_temperaturas(lista):
    return list(map(lambda c: (c * 9/5) + 32, lista))

def calificaciones_a_letras(lista):
    def convertir(nota):
        if nota >= 90: return 'A'
        elif nota >= 80: return 'B'
        elif nota >= 70: return 'C'
        elif nota >= 60: return 'D'
        else: return 'F'
    return list(map(convertir, lista))

def contar_palabras(texto):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def buscar_elemento(lista, elemento):
    return next((i for i, val in enumerate(lista) if val == elemento), -1)

def validar_parentesis(secuencia):
    balance = 0
    for char in secuencia:
        if char == '(': balance += 1
        elif char == ')': balance -= 1
        if balance < 0: return False
    return balance == 0

def ordenar_tuplas(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))

def generar_contrasena(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def agenda_telefonica():
    agenda = {}
    while True:
        print("\n1. Agregar contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Mostrar contactos\n5. Volver al menú principal")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
        elif opcion == '2':
            nombre = input("Nombre: ")
            print("Teléfono:", agenda.get(nombre, "No encontrado"))
        elif opcion == '3':
            nombre = input("Nombre: ")
            agenda.pop(nombre, None)
        elif opcion == '4':
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida")

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Calculadora\n2. Filtrar números pares\n3. Convertir temperaturas\n4. Convertir calificaciones a letras\n5. Contar palabras en un texto")
        print("6. Buscar elemento en lista\n7. Validar paréntesis\n8. Ordenar lista de tuplas\n9. Generar contraseña\n10. Gestión de agenda telefónica\n11. Salir")

        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            calculadora()
        elif opcion == '2':
            lista = list(map(int, input("Ingrese números separados por espacio: ").split()))
            print("Números pares:", filtrar_pares(lista))
        elif opcion == '3':
            lista = list(map(float, input("Ingrese temperaturas en Celsius separadas por espacio: ").split()))
            print("Temperaturas en Fahrenheit:", convertir_temperaturas(lista))
        elif opcion == '4':
            lista = list(map(int, input("Ingrese calificaciones numéricas separadas por espacio: ").split()))
            print("Calificaciones en letras:", calificaciones_a_letras(lista))
        elif opcion == '5':
            texto = input("Ingrese un texto: ")
            print("Conteo de palabras:", contar_palabras(texto))
        elif opcion == '6':
            lista = input("Ingrese elementos separados por espacio: ").split()
            elemento = input("Elemento a buscar: ")
            print("Índice:", buscar_elemento(lista, elemento))
        elif opcion == '7':
            secuencia = input("Ingrese una secuencia de paréntesis: ")
            print("Secuencia válida:" if validar_parentesis(secuencia) else "Secuencia no válida")
        elif opcion == '8':
            lista = []
            while True:
                entrada = input("Ingrese nombre y edad (o 'fin' para terminar): ")
                if entrada.lower() == 'fin': break
                nombre, edad = entrada.rsplit(maxsplit=1)
                lista.append((nombre, int(edad)))
            print("Lista ordenada:", ordenar_tuplas(lista))
        elif opcion == '9':
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            print("Contraseña generada:", generar_contrasena(longitud))
        elif opcion == '10':
            agenda_telefonica()
        elif opcion == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()

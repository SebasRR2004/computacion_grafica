import math

def caida_libre(h):
    """
    Función que calcula el tiempo que tarda un objeto en caer desde una altura dada bajo la influencia de la gravedad.

    Parámetros:
    h (float): Altura desde la que cae el objeto en metros.

    Retorna:
    float: Tiempo en segundos que tarda el objeto en llegar al suelo.
    """
    g = 9.81  # Definimos la aceleración gravitacional en la Tierra en m/s^2.
    t = math.sqrt((2 * h) / g)  # Aplicamos la fórmula del tiempo de caída libre: t = sqrt(2h/g).
    return t  # Retornamos el tiempo calculado.

def conversion_velocidad(valor, tipo):
    """
    Función para convertir unidades de velocidad entre km/h y m/s y viceversa.

    Parámetros:
    valor (float): Valor de la velocidad a convertir.
    tipo (str): Tipo de conversión. Puede ser "kmh_a_ms" para convertir de km/h a m/s o "ms_a_kmh" para la conversión inversa.

    Retorna:
    float: Velocidad convertida o None si el tipo de conversión no es válido.
    """
    if tipo == "kmh_a_ms":  # Si el usuario quiere convertir de km/h a m/s...
        return valor / 3.6  # Dividimos por 3.6 porque 1 km/h equivale a 1/3.6 m/s.
    elif tipo == "ms_a_kmh":  # Si el usuario quiere convertir de m/s a km/h...
        return valor * 3.6  # Multiplicamos por 3.6 porque 1 m/s equivale a 3.6 km/h.
    else:
        return None  # Si el tipo de conversión no es válido, retornamos None.

def calculo_desplazamiento(u, a, t):
    """
    Calcula el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado (MRUA) utilizando la ecuación del movimiento.

    Parámetros:
    u (float): Velocidad inicial en m/s.
    a (float): Aceleración en m/s^2.
    t (float): Tiempo en segundos.

    Retorna:
    float: Desplazamiento en metros.
    """
    s = (u * t) + (0.5 * a * t**2)  # Se aplica la fórmula del desplazamiento: s = ut + 1/2 * a * t^2.
    return s  # Se retorna el valor calculado.

def suma_vectores(v1, v2):
    """
    Realiza la suma de dos vectores bidimensionales representados como listas.

    Parámetros:
    v1 (list): Primer vector [x1, y1].
    v2 (list): Segundo vector [x2, y2].

    Retorna:
    list: Vector resultante de la suma [x1 + x2, y1 + y2].
    """
    return [v1[0] + v2[0], v1[1] + v2[1]]  # Se suman las componentes respectivas de cada vector.

def producto_escalar(v1, v2):
    """
    Calcula el producto escalar de dos vectores bidimensionales y el ángulo entre ellos en grados.

    Parámetros:
    v1 (list): Primer vector [x1, y1].
    v2 (list): Segundo vector [x2, y2].

    Retorna:
    tuple: Producto escalar (float) y ángulo en grados (float).
    """
    escalar = v1[0] * v2[0] + v1[1] * v2[1]  # Se calcula el producto escalar de los vectores.
    magnitud_v1 = math.sqrt(v1[0]**2 + v1[1]**2)  # Se calcula la magnitud del primer vector.
    magnitud_v2 = math.sqrt(v2[0]**2 + v2[1]**2)  # Se calcula la magnitud del segundo vector.
    angulo = math.acos(escalar / (magnitud_v1 * magnitud_v2)) * (180 / math.pi)  # Se usa arccos para obtener el ángulo en radianes y se convierte a grados.
    return escalar, angulo  # Se retorna el producto escalar y el ángulo calculado.

def lanzamiento_proyectil(v0, angulo):
    """
    Calcula el alcance y la altura máxima de un proyectil lanzado con un ángulo y una velocidad inicial dada.

    Parámetros:
    v0 (float): Velocidad inicial en m/s.
    angulo (float): Ángulo de lanzamiento en grados.

    Retorna:
    tuple: Alcance máximo (float) y altura máxima (float).
    """
    g = 9.81  # Definimos la gravedad en la Tierra en m/s^2.
    angulo_rad = math.radians(angulo)  # Convertimos el ángulo de grados a radianes.
    alcance = (v0**2 * math.sin(2 * angulo_rad)) / g  # Se calcula el alcance usando la ecuación correspondiente.
    altura_max = (v0**2 * math.sin(angulo_rad)**2) / (2 * g)  # Se calcula la altura máxima.
    return alcance, altura_max  # Se retorna el alcance y la altura máxima.


def menu():
    while True:
        print("\nMenu de Opciones:")
        print("1. Calculo de la Caida Libre")
        print("2. Conversion de Unidades de Velocidad")
        print("3. Calculo del Desplazamiento")
        print("4. Suma de Vectores")
        print("5. Producto Escalar de Vectores")
        print("6. Lanzamiento de Proyectil")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            while True:
                try:
                    h = float(input("Ingrese la altura (m): "))
                    if h < 0:
                        print("La altura no puede ser negativa. Intente nuevamente.")
                        continue
                    print(f"Tiempo de caída: {caida_libre(h):.2f} s")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")
        elif opcion == "2":
            while True:
                try:
                    valor = float(input("Ingrese la velocidad: "))
                    tipo = input("Ingrese el tipo de conversión (kmh_a_ms / ms_a_kmh): ")
                    if tipo not in ["kmh_a_ms", "ms_a_kmh"]:
                        print("Tipo de conversión inválido. Intente nuevamente.")
                        continue
                    resultado = conversion_velocidad(valor, tipo)
                    print(f"Velocidad convertida: {resultado:.2f}")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")
        elif opcion == "3":
            while True:
                try:
                    u = float(input("Ingrese la velocidad inicial (m/s): "))
                    a = float(input("Ingrese la aceleración (m/s^2): "))
                    t = float(input("Ingrese el tiempo (s): "))
                    print(f"Desplazamiento: {calculo_desplazamiento(u, a, t):.2f} m")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese números válidos.")
        elif opcion == "4":
            while True:
                try:
                    v1 = list(map(float, input("Ingrese el primer vector (x y): ").split()))
                    v2 = list(map(float, input("Ingrese el segundo vector (x y): ").split()))
                    print(f"Suma de vectores: {suma_vectores(v1, v2)}")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese números válidos.")
        elif opcion == "5":
            while True:
                try:
                    v1 = list(map(float, input("Ingrese el primer vector (x y): ").split()))
                    v2 = list(map(float, input("Ingrese el segundo vector (x y): ").split()))
                    escalar, angulo = producto_escalar(v1, v2)
                    print(f"Producto escalar: {escalar:.2f}, Ángulo: {angulo:.2f}°")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese números válidos.")
        elif opcion == "6":
            while True:
                try:
                    v0 = float(input("Ingrese la velocidad inicial (m/s): "))
                    angulo = float(input("Ingrese el ángulo (grados): "))
                    alcance, altura_max = lanzamiento_proyectil(v0, angulo)
                    print(f"Alcance máximo: {alcance:.2f} m, Altura máxima: {altura_max:.2f} m")
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese números válidos.")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()

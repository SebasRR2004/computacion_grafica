import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
print(os.getcwd())  # Esto muestra la ruta actual del script


# 1. Creación y Manipulación de Arrays
A = np.arange(1, 16).reshape(3, 5)
print("Array A:\n", A)

# 2. Operaciones Básicas
suma = np.sum(A)
media = np.mean(A)
producto = np.prod(A)
print("Suma de A:", suma)
print("Media de A:", media)
print("Producto de A:", producto)

# 3. Acceso y Slicing
segundo_tercer_elemento_segunda_fila = A[1, 1:3]
print("Segundo y tercer elemento de la segunda fila de A:", segundo_tercer_elemento_segunda_fila)

# 4. Indexación Booleana
B = A[A > 7]
print("Array B con elementos de A mayores que 7:\n", B)

# 5. Álgebra Lineal
C = np.random.randint(1, 10, size=(3, 3))
determinante_C = np.linalg.det(C)
inversa_C = np.linalg.inv(C)
print("Matriz C:\n", C)
print("Determinante de C:", determinante_C)
print("Inversa de C:\n", inversa_C)

# 6. Estadísticas con NumPy
D = np.random.rand(100)
max_D = np.max(D)
min_D = np.min(D)
media_D = np.mean(D)
std_D = np.std(D)
print("Array D:\n", D)
print("Máximo de D:", max_D)
print("Mínimo de D:", min_D)
print("Media de D:", media_D)
print("Desviación estándar de D:", std_D)

# 7. Gráfico Básico
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure()
plt.plot(x, y_sin, label='Seno')
plt.plot(x, y_cos, label='Coseno')
plt.legend()
plt.title("Seno y Coseno")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# 8. Gráficos de Dispersión
plt.figure()
plt.scatter(range(len(D)), D)
plt.title("Gráfico de Dispersión de D")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.show()

# 9. Histogramas
plt.figure()
plt.hist(D, bins=20)
plt.title("Histograma de D")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# 10. Manipulación de Imágenes con Matplotlib
img = mpimg.imread(r'C:\Users\Sebastián\Documents\Ingeniería\Computación Gráfica\computacion_grafica\Talleres\imagen.jpg')
img_gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Imagen Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title("Imagen en Escala de Grises")
plt.axis('off')

plt.show()
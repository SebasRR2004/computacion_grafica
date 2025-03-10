import numpy as np
from scipy import stats

# 1. Cree el vector A= [2, 3, 5, 1, 4 ,7 9, 8, 6, 10]
A = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])

# 2. Cree un vector B que contenga los elementos desde el 11 hasta el 20
B = np.arange(11, 21)

# 3. Componer un vector C formado por los vectores A y B en la misma fila respectivamente
C = np.concatenate((A, B))

# 4. Encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy
valor_minimo = np.min(C)

# 5. Encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy
valor_maximo = np.max(C)

# 6. Encuentre la longitud en el vector C haciendo uso de la función propia de Numpy
longitud = len(C)

# 7. Encuentre el promedio de los elementos en el vector C haciendo uso de las operaciones elementales suma y división
promedio_manual = np.sum(C) / longitud

# 8. Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy
promedio_numpy = np.mean(C)

# 9. Encuentre la media en el vector C haciendo uso de la función propia de Numpy
mediana = np.median(C)

# 10. Encuentre la suma en el vector C haciendo uso de la función propia de Numpy
valor_suma = np.sum(C)

# 11. Cree un vector D a partir del vector C con los elementos mayores que 5
D = C[C > 5]

# 12. Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15
E = C[(C > 5) & (C < 15)]

# 13. Cambie los elementos 5 y 15 elemento del vector C por ‘7’
C[C == 5] = 7
C[C == 15] = 7

# 14. Determine la moda del vector C
moda = stats.mode(C)[0][0]

# 15. Ordene el Vector C de menor a mayor
C_ordenado = np.sort(C)

# 16. Multiplique el vector C por 10
C_multiplicado = C * 10

# 17. Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente
C[5:8] = [60, 70, 80]

# 18. Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente
C[13:16] = [140, 150, 160]

# Imprimir resultados
print("Vector A:", A)
print("Vector B:", B)
print("Vector C:", C)
print("Valor mínimo de C:", valor_minimo)
print("Valor máximo de C:", valor_maximo)
print("Tamaño de C:", longitud)
print("Promedio (manual) de C:", promedio_manual)
print("Promedio (numpy) de C:", promedio_numpy)
print("Mediana de C:", mediana)
print("Suma de C:", valor_suma)
print("Vector D (elementos > 5):", D)
print("Vector E (elementos > 5 y < 15):", E)
print("Moda de C:", moda)
print("C ordenado:", C_ordenado)
print("C multiplicado por 10:", C_multiplicado)
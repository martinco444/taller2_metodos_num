import numpy as np
import math 

#ejercicio 1
# Definir la función
def f(x):
    return math.sqrt(x**3 + 1)

a = 1
b = 4
n = 4
deltaX = (b - a) / n 
X = np.linspace(a, b, n+1)

sum_par = 0
sum_impar = 0

# Cálculo de sumas de pares e impares
for i in range(1, len(X)-1):
    if i % 2 == 0:
        print("sum par", i)
        sum_par += f(X[i])
    else:
        sum_impar += f(X[i])
        print("sum impar", i)

I = (deltaX / 3) * (f(X[0]) + 4*sum_impar + 2*sum_par + f(X[n]))

print("respuesta ejercicio 1:")
print(I, "\n")
#--------------------------------------------------------------------------------------------------
#ejercicio 2

X = np.array([1.0, 2.0, 3.0, 4.0])  # Puntos x
Y = np.array([2.0, 3.0, 5.0, 4.0])  # Valores f(x)

n = len(X)
A = np.zeros((n, n))
A[:, 0] = Y  


for k in range(1, n):
    for i in range(k, n):
        A[i, k] = (A[i, k-1] - A[i-1, k-1]) / (X[i] - X[i-k])

print("Tabla de diferencias divididas de Newton:\n", A, "\n")

# Definir el polinomio de interpolación de Newton
def newton_polynomial(X, A, x):
    n = len(X)
    poly = A[0, 0]  
    for i in range(1, n):
        term = A[i, i]  
        for j in range(i):
            term *= (x - X[j])  
        poly += term  
    return poly

x_eval = 2.6
interp_value = newton_polynomial(X, A, x_eval)

print("respuesta ejercicio 2:")
print(interp_value, "\n")

#--------------------------------------------------------------------------------------------------
#ejercicio 3

# Nodos y valores de f(x) proporcionados
X = np.array([1.0, 2.0, 3.0])  # Valores de x
Y = np.array([2.0, 3.0, 5.0])  # Valores de f(x)

# Valor donde evaluaremos el polinomio (x = 2.6)
x = 2.6

# Inicializar el polinomio de interpolación
polinomio_n = 0

# Cálculo del polinomio de Lagrange
n = len(X) - 1  # Grado del polinomio es len(X)-1
for i in range(0, n + 1):
    productoria = 1
    for j in range(0, n + 1):
        if j != i:
            productoria *= (x - X[j]) / (X[i] - X[j])
    
    # Sumar el término correspondiente a f(X[i]) * L_i(x)
    polinomio_n += productoria * Y[i]

print("respuesta ejercicio 3:")
print(polinomio_n, "\n")

#--------------------------------------------------------------------------------------------------
#ejercicio 4

import numpy as np

# Definir la función f(x) = 3^x
def f(x):
    return 3 ** x

X = np.array([1.0, 1.5, 2.0])  

x = 1.732 

polinomio_n = 0

# Cálculo del polinomio de Lagrange
n = len(X) - 1  
for i in range(0, n + 1):
    productoria = 1
    for j in range(0, n + 1):
        if j != i:
            productoria *= (x - X[j]) / (X[i] - X[j])
    
    polinomio_n += productoria * f(X[i])

print("La respuesta del ejercicio 4 es:")
print(polinomio_n, "\n")

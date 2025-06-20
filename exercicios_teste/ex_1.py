'''
Calculcar os valores da função senx*cosx para x= 0, 0.001, 0.002, ... 2π.
'''

import math

# Definir o intervalo de valores de x
x_values = [i*0.001 for i in range(int(2*math.pi/0.001)+1)]

# Calcular sen(x) * cos(x) para cada valor de x
results = [(x, math.sin(x)*math.cos(x))for x in x_values]

# exibir os resultados
for x, result in results:
    print(f'x={x:.3f},sin(x)*cos(x)={result:.6f}')

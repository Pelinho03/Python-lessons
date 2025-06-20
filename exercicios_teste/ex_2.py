'''
Calcular o valor máximo e mínimo da função sen x - cos x, no intervalo [0, 2π].
Usar passo de 0.001.
'''

import math

# Definir o intervalo e o passo
x_values = [i*0.001 for i in range(int(2*math.pi/0.001)+1)]

# Calcular os valores da função
results = [(x, math.sin(x) - math.cos(x)) for x in x_values]

# Encontrar o valor máximo e mínimo
max_value = max(results, key=lambda item: item[1])
min_value = min(results, key=lambda item: item[1])

# Exibir os resultados
print(
    f'Valor máximo: x = {max_value[0]:.3f},sin(x) -cos(x)={max_value[1]:.6f}')
print(
    f'Valor mínimo: x = {min_value[0]:.3f},sin(x) -cos(x)={min_value[1]:.6f}')

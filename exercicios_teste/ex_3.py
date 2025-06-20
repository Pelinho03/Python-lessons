'''
Dado x>=0, determinar para qual K, o valor de e^x /K! fica menor que 10^-5
'''
import math


def encontrar_k(x, limite=1e-5):
    k = 0
    while True:
        termo = math.exp(x) / math.factorial(k)
        if termo < limite:
            return k
        k += 1


# Teste com valor de x
x = float(input('Digite o valor de x: '))
k_encontrado = encontrar_k(x)
print(f'O menor k para o qual e^{x}/k!<10^-5 é {k_encontrado}')

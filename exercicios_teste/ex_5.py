'''
Dado N, simule a jogada de um dado (faces 1 a 6) N vezes e calcule quantas vezes cada face ocorreu.
'''

import random
from collections import Counter


def simular_dado(n):
    resultados = [random.randint(1, 6)
                  for _ in range(n)]  # Gera N jogadas do dado
    contagem = Counter(resultados)  # Conta a ocorrência de cada face

    # Exibir os resultados
    print('Resultados das jogadas: ')
    for face in range(1, 7):
        print(f'Face {face}: {contagem[face]} vezes')


# Teste com valor de N
N = int(input('Digite o número de jogadas do dado: '))
simular_dado(N)

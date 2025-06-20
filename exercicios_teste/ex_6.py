'''
Dados i e j (1<=i, j<=6), simule a jogada de 2 dados 1000 vezes e diga quantas vezes ocorreu o par i, j de faces.
'''

import random


def contar_par_ocorrencias(i, j, num_jogadas=1000):
    ocorrencias = 0

    for _ in range(num_jogadas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        if (dado1, dado2) == (i, j):
            ocorrencias += 1

    return ocorrencias


# Dados de entrada
i = int(input("Digite o valor de i (1-6): "))
j = int(input("Digite o valor de j (1-6): "))

# Verificar os valores de entrada
if 1 <= i <= 6 and 1 <= j <= 6:
    resultado = contar_par_ocorrencias(i, j)
    print(f'O par ({i}, {j}) ocorreu {resultado} vezes em 1000 jogadas.')
else:
    print('Os valores de i e j devem ser entre 1 e 6.')

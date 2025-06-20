'''
Dado n inteiro e x real, calcular o valor da soma 1 + x + x^2 + x^3 + ... + x^n.
Para resolver sem usar a fórmula de soma de Progressão Geométrica
(Sm = (a1 * (q^m 1)) / ( q-1)) e sem usar a função pow.
'''


def calcular_soma(n, x):
    soma = 1  # Primeiro termo é sempre 1
    termo = 1  # Inicializamos o termo como 1 (x^0)

    for i in range(1, n+1):
        termo *= x  # Calculamos x^i manualmente
        soma += termo  # Somamos ao total

    return soma


# Dados de entrar
n = int(input('Digite um valor inteiro para n: '))
x = float(input('Digite um valor real para x: '))

# Calcular a soma
resultado = calcular_soma(n, x)
print(f'A soma de 1+x+x^2+...+x^{n} é: {resultado:.6f}')

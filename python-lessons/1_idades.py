'''
Escreva um programa que a partir da 
idade de uma pessoa expressa em anos, 
meses e dias, apresente a idade apenas
em dias (considerar o ano com 365 dias e
cada mês com 30 dias).
'''
# Função para ler um número inteiro positivo com validação


def ler_inteiro_positivo(pergunta, limite_max=None):
    while True:
        try:
            valor = int(input(pergunta))
            if valor < 0:
                print("Por favor, introduz um valor **positivo**.")
            elif limite_max is not None and valor > limite_max:
                print(
                    f"Por favor, introduz um valor inferior ou igual a {limite_max}.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Tenta novamente com um número inteiro.")


# Ler dados com validação
anos = ler_inteiro_positivo('Quantos anos de idade tens? ')
meses = ler_inteiro_positivo(
    'Quantos meses além dos anos completos? (0 a 11) ', limite_max=11)
dias = ler_inteiro_positivo(
    'Quantos dias além dos meses completos? (0 a 29) ', limite_max=29)

# Calcular idade total em dias
total_dias = anos * 365 + meses * 30 + dias

# Mostrar resultado
print(f'\nA tua idade em dias é: {total_dias}')

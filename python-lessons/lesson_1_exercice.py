#Criar um programa que permita ao utilizador adivinhar um número secreto gerado aleatóriamente enre 1 e 100. 
#O jogador tem no máximo 10 tentativas para adivinhar o número.
#Após cada tentativas, o programa deve informar se o número é maior ou menor que o número secreto.
#No final, o programa deve exibir uma mensahem indicando se o jogador ganhou ou perdeu.


import random
tentativas=0

numero_secreto=random.randint(1,100)
for i in range(1,10):
    aposta=int(input("\nAdivinha o número secreto: "))
    if aposta==numero_secreto:
        print('\nParabéns, venceste!')
        print(f'O número secreto é: {numero_secreto}')
        break
    elif aposta>numero_secreto:
        print('\nO número secreto é menor')
        print(f'tenativa nº {i}')
        tentativas+=1
        print(f'Tentativas restantes: {10-tentativas}')
    elif aposta<numero_secreto:
        print('\nO número secreto é maior')        
        print(f'tenativa nº {i}')
        tentativas+=1
        print(f'Tentativas restantes: {10-tentativas}')
    else:
        print('\nNúmero Inválido!')

print('Fim do jogo!')


import random

numsecreto=random.randint(1,100)
tentativas=10

while tentativas>0:
    aposta=int(input("Qual é o seu palpite? "))
    if aposta==numsecreto:
        print("\nParabéns! Ganhaste!")
        break
    elif aposta<numsecreto:
        print("\nO número secreto é maior.")
    else:
        print("\nO número secreto é menor.")
    tentativas-=1
    print(f'\nAinda tens {tentativas} tentativas.')
if tentativas==0:
    print(f'\nO número secreto era {numsecreto}.')
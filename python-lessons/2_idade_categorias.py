'''
Escreva um programa que receba a idade de um atleta e
determine a sua categoria segundo a tabela apresentada:
Categoria Idade
Infantil 5 - 7 anos
Iniciado 8 - 10 anos
Juvenil 11 - 13 anos
Junior 14 - 17 anos
Sénior Maiores de 18 anos
'''
idade = int(input('Digita a tua idade: '))

try:
    idade = int(input('Digita a tua idade: '))
    if idade < 0:
        print('A idade não pode ser negativa.')
    elif 5 <= idade <= 7:
        print(f'Com {idade} anos, pertences à categoria "Infantil".')
    elif 8 <= idade <= 10:
        print(f'Com {idade} anos, pertences à categoria "Iniciado".')
    elif 11 <= idade <= 13:
        print(f'Com {idade} anos, pertences à categoria "Juvenil".')
    elif 14 <= idade <= 17:
        print(f'Com {idade} anos, pertences à categoria "Junior".')
    elif idade >= 18:
        print(f'Com {idade} anos, pertences à categoria "Sénior".')
    else:
        print(f'Com {idade} anos, ainda não pertences a nenhuma categoria.')
except ValueError:
    print('Por favor, introduz um número inteiro válido.')

'''
O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira
simplificada de identificá-lo é verificando-se apenas o ano de seu nascimento do seguinte 
modo.
'''

zodiaco_chines = [
    "MACACO", "GALO", "CÃO", "PORCO", "RATO", "BOI",
    "TIGRE", "COELHO", "DRAGÃO", "SERPENTE", "CAVALO", "CARNEIRO"
]  # 0 1 2 3 4 5 6 7 8 9 10 11

try:
    anoNascimento = int(input("Digita o teu ano de nascimento: "))
    indice = anoNascimento % 12
    animal = zodiaco_chines[indice]
    print(f"Nascido em {anoNascimento} és do tipo {animal}!")
except ValueError:
    print("VALOR INCORRETO!")

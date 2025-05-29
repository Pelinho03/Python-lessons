'''
Escreva um programa que permita registar o nome, a
altura e o peso de duas pessoas e apresente o nome
da mais pesada e o nome da mais alta.
'''
# Listas para guardar os dados
nomes = []
alturas = []
pesos = []

maisPesada = 0
maisAlta = 0
nomeMaisPesada = ""
nomeMaisAlta = ""

# Registar dados de 2 pessoas
for i in range(2):
    print(f"\nPessoa {i + 1}:")
    nome = input("Digita o teu nome: ")
    altura = int(input("Digita a tua altura em cm: "))
    peso = int(input("Digita o teu peso em kg: "))

    nomes.append(nome)
    alturas.append(altura)
    pesos.append(peso)

# Verificar a mais pesada e mais alta
for i in range(len(nomes)):
    if pesos[i] > maisPesada:
        maisPesada = pesos[i]
        nomeMaisPesada = nomes[i]
    if alturas[i] > maisAlta:
        maisAlta = alturas[i]
        nomeMaisAlta = nomes[i]

# Mostrar resultados
print(f"\nA pessoa mais pesada é: {nomeMaisPesada}")
print(f"A pessoa mais alta é: {nomeMaisAlta}")

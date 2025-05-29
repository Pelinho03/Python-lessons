'''
Escreva um programa para determinar a situação de um aluno 
(Aprovado/Exame/Reprovado) dada a sua assiduidade em
percentagem e a nota do teste (0 a 20), considerando a seguinte tabela:
Condição Situação
Assiduidade inferior a 75% Reprovado
Assiduidade entre 75% e 100% e nota até 5 Reprovado
Assiduidade entre 75% e 100% e nota de 5 até 9,4 Exame
Assiduidade entre 75% e 100% e nota entre 9,5 e 20 Aprovado
'''

faltas = int(input('Digita o nº de faltas no semestre: '))
nota = float(input('Digita a nota obtida no teste: '))

totalAulas = 20
assiduidade = ((totalAulas - faltas) * 100) / totalAulas

if assiduidade < 75:
    print(f'Com assiduidade de {assiduidade:.1f}% está: REPROVADO!')
elif assiduidade <= 100 and nota <= 5:
    print(
        f'Com assiduidade de {assiduidade:.1f}% e nota de {nota} está: REPROVADO!')
elif assiduidade <= 100 and 5 < nota < 9.5:
    print(
        f'Com assiduidade de {assiduidade:.1f}% e nota de {nota} está: EXAME!')
elif assiduidade <= 100 and nota >= 9.5 and nota <= 20:
    print(
        f'Com assiduidade de {assiduidade:.1f}% e nota de {nota} está: APROVADO!')
else:
    print('ERRO: Valores inválidos.')

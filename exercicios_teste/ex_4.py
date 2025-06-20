'''
Construa uma tabela para x = 0, 0.01, 0.02, ..., 0.10 com o valor de x^1, x^2, ..., x^10.
'''

x_values = [round(i*0.01, 2) for i in range(11)]  # Corrigido o passo

print('  x |', '|'.join([f'x^{i}' for i in range(1, 11)]))
print('-'*80)

for x in x_values:
    row = [f'{x:.2f}'] + [f'{x**(i+1):.5f}' for i in range(10)]
    print(' | '.join(row))

n1 = float(input('Nota da 1ª avaliação: '))
n2 = float(input('Nota da 2ª avaliação: '))

m = (n1 + n2) / 2
print(f'Média do aluno: {m:.2f}')

if m < 5.0:
    print('Resultado: REPROVADO')
elif 5.0 <= m < 7:
    print('Resultado: RECUPERAÇÃO')
else:
    print('Resultado: APROVADO')

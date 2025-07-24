print('+' * 20)
print('CALCULADORA DE MÉDIA')
print('+' * 20)

nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))

media = (nota1 + nota2) / 2

print(f'Média do aluno: {media:.2f}')

if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

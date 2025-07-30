maioresde18 = totalhomens = mulheresmenos20anos = 0

while True:
    print('-' * 25)
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('-' * 25)
    # idade
    idade = int(input('Idade: '))
    # sexo
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'Mm' and sexo not in 'Ff':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # estatísticas
    if idade > 18:
        maioresde18 += 1
    if sexo in 'Mm':
        totalhomens += 1
    if sexo in 'Fm' and idade < 20:
        mulheresmenos20anos += 1
    # continuidade do programa
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'Ss' and resp not in 'Nn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
# Relatório final
print(f'{" FIM DO PROGRAMA ":=^30}')
print(f'Total de pessoas com mais de 18 anos: {maioresde18}')
print(f'Ao todo temos {totalhomens} homens cadastrados')
print(f'E temos {mulheresmenos20anos} mulheres com menos de 20 anos')

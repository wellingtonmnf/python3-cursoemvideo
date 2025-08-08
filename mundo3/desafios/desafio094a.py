pessoas = list()
mulheres = list()
idade_acima_da_media = list()
soma_idades = total_pessoas = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if resp == 'N':
        break

print(f'Total de pessoas cadastradas: {len(pessoas)}')

for p in pessoas:
    soma_idades += p['idade']
    total_pessoas += 1

    if p['sexo'] in 'F':
        mulheres.append(p['nome'])

media_idade = soma_idades / total_pessoas

for pes in pessoas:
    if pes['idade'] > media_idade:
        idade_acima_da_media.append(pes['nome'])

print('-' * 40)
print(f'A média de idade do grupo é de {media_idade:.2f} anos')
print(f'As mulheres do grupo são: {mulheres}')
print(f'As pessoas com idade acima da média são: {idade_acima_da_media}')

dados = {}
pessoas = []
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.', end=' ')
        else:
            break
    if resp == 'N':
        break
soma_idade = 0
for p in pessoas:
    soma_idade += p['idade']
media_idade = soma_idade / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram:')
for pes in pessoas:
    if pes['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for pes in pessoas:
    if pes['idade'] > media_idade:
        print(pes)
print('<< ENCERRADO >>')

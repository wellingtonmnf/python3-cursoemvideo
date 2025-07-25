print('-' * 35)
print(f'{"ANALISADOR DE PESSOAS":^35}')
print('-' * 35)

somaidade = 0
idadehomemmaisvelho = 0
mulherescommenosdevinte = 0

for c in range(1, 5):
    print(f'Insira os dados da {c}ª pessoa:')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()
    print('-' * 35)
    # Somatório da idade para o cálculo da média
    somaidade += idade
    # Checando a idade do homem mais velho
    if sexo == 'M':
        if idade >= idadehomemmaisvelho:
            idadehomemmaisvelho = idade
            nomehomemmaisvelho = nome
    # checando quantas mulheres possuem menos de 20 anos
    if sexo == 'F':
        if idade < 20:
            mulherescommenosdevinte += 1

mediaidade = somaidade / 4

print('-' * 35)
print(f'{"RESULTADO DA ANÁLISE":^35}')
print(f'Média de idade do grupo: {mediaidade:.0f} anos')
print(f'Nome do homem mais velho: {nomehomemmaisvelho}')
print(f'Mulheres com menos de 20 anos: {mulherescommenosdevinte}')
print('-' * 35)

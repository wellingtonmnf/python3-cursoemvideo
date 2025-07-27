somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range(1,5):
    print(f'{" {}ª PESSOA ":—^21}'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    # Somando as idades do grupo para calcular a média
    somaidade += idade
    # Checagem de homens e suas idades
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    # Checagem de mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade/4

print(f'{" RELATÓRIO ":—^21}')
print(f'A média de idade do grupo é de {mediaidade:.1f} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos')

nomes = []
notas = [[], []]
medias = []
alunos = [nomes, notas, medias]

while True:
    # Lendo dados do usuário
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # Adicionando dados nas listas
    nomes.append(nome)
    notas[0].append(nota1)
    notas[1].append(nota2)
    medias.append(media)
    # Confirmação de continuidade do programa
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if resp == 'N':
        break

print('-' * 25)
print('BOTELIM'.center(25))
print('-' * 25)
print('Nº   NOME           MÉDIA')
print('-' * 25)
# Lendo os dados no botelim
for c in range(0, len(nomes)):
    print(f'{c:>003}  {alunos[0][c]:<15}{alunos[2][c]:>5.2f}')
# Mostrando as notas individuais de cada aluno
while True:

    print('-' * 25)
    num_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if num_aluno == 999:
        print('FINALIZANDO...')
        print('VOLTE SEMPRE!'.center(25, '-'))
        break
    elif num_aluno < len(nomes):
        print(f'Notas de {alunos[0][num_aluno]} são {alunos[1][0][num_aluno], alunos[1][1][num_aluno]}')
    else:
        print('Aluno não consta no banco de dados')

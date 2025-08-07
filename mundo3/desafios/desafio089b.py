alunos = list()

while True:
    # Lendo dados do usuário
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # Adicionando dados nas listas
    alunos.append([nome, [nota1, nota2], media])
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
for pos, aluno in enumerate(alunos):
    print(f'{pos:>003}  {aluno[0]:<15}{aluno[2]:>5.2f}')
# Mostrando as notas individuais de cada aluno
while True:

    print('-' * 25)
    num_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if num_aluno == 999:
        print('FINALIZANDO...')
        print('VOLTE SEMPRE!'.center(25, '-'))
        break
    elif num_aluno < len(alunos):
        print(f'Notas de {alunos[num_aluno][0]} são {alunos[num_aluno][1]}')
    else:
        print('Aluno não consta no banco de dados')

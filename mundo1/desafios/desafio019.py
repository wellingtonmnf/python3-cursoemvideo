import random

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sort = random.randint(0, 3)

print(f'O aluno que apagará o quadro é o {sort}º aluno: {lista[sort]}')




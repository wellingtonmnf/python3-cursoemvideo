from random import choice

a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')

lista = [a1, a2, a3, a4]
x = choice(lista)

print('O aluno que irá apagar o quadro será: {}'.format(x))

nome = 'José'
idade = 33
salario = 987.65

print(f'O {nome} tem {idade} anos.')  # PYTHON 3.6.3
print('O {} tem {} anos.'.format(nome, idade))  # PYTHON 3
print(('O %s tem %d anos.' % (nome, idade)))  # PYTHON 2

print(f'O {nome} tem {idade} anos e ganha R$ {salario}')
print(f'O {nome:20} tem {idade} anos e ganha R$ {salario:.2f}') # determina caracteres
print(f'O {nome:^20} tem {idade} anos e ganha R$ {salario:.2f}') # centraliza
print(f'O {nome:-^20} tem {idade} anos e ganha R$ {salario:.2f}') # centraliza e complementa
print(f'O {nome:->20} tem {idade} anos e ganha R$ {salario:.2f}') # alinha à direita
print(f'O {nome:-<20} tem {idade} anos e ganha R$ {salario:.2f}') # alinha à esquerda

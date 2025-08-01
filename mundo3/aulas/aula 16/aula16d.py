lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # tupla

print(len(lanches))

for comida in lanches:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-' * 30)

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba!')

print('-' * 30)

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posição {cont}')

print('-' * 30)

for c in range(len(lanches) - 1, -1, -1):
    print(f'Eu vou comer {lanches[c]} na posição {c}')

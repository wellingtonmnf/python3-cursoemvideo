from random import randint
from time import sleep

print('-' * 9)
print('JO-KEN-PÔ')
print('-' * 9)

jokenpo = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}
maquina = randint(1,3)
print('ESCOLHA: 1 - PEDRA | 2 - PAPEL | 3 - TESOURA')
usuario = int(input('Digite a opção escolhida: '))

if usuario > 3 or usuario <= 0:
    print('OPÇÃO INVÁLIDA!')
else:
    print('PROCESSANDO...')
    sleep(1)
    print(f'MÁQUINA ESCOLHEU: {jokenpo[maquina]} X USUÁRIO ESCOLHEU: {jokenpo[usuario]}')

    if maquina == usuario:
        print('EMPATE!')
    elif maquina == 1 and usuario == 2:
        print('USUÁRIO VENCEU!')
    elif maquina == 1 and usuario == 3:
        print('MÁQUINA VENCEU!')
    elif maquina == 2 and usuario == 1:
        print('MÁQUINA VENCEU!')
    elif maquina == 2 and usuario == 3:
        print('USUÁRIO VENCEU!')
    elif maquina == 3 and usuario == 1:
        print('USUÁRIO VENCEU!')
    elif maquina == 3 and usuario == 2:
        print('MÁQUINA VENCEU!')

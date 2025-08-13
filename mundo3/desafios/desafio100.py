from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(0, 5):
        num = randint(0, 10)
        print(num, end=' ')
        sleep(0.25)
        numeros.append(num)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores de {lista}, temos {s}')

numeros = list()
sorteia()
somaPar(numeros)

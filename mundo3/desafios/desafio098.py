from time import sleep


def contador(inicio, final, passo):
    print('-' * 35)
    print(f'Contagem de {inicio} até {final}', end=' ')
    if passo == 0:
        passo = 1
    if inicio > final:
        final -= 1
        if passo < 0:
            print(f'de {passo * -1} em {passo * -1}:')
        else:
            print(f'de {passo} em {passo}:')
            passo = passo * -1
    else:
        if (inicio < final and passo < 0) or inicio == final:
            print(f'de {passo} em {passo}:')
            print('Essa contagem não pode ser feita!')
        else:
            final += 1
            print(f'de {passo} em {passo}:')
    for n in range(inicio, final, passo):
        print(n, end=' ')
        sleep(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 35)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

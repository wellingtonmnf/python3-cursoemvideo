from time import sleep


def contador(inicio, fim, passo):
    if (inicio < fim and passo < 0) or inicio == fim:
        print('Essa contagem não pode ser feita!')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='')
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c} ', end='')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 35)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

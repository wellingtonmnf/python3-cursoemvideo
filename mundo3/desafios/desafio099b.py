from time import sleep

def maior(*num):
    print('-' * (35 + len(num) * 2))
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.25)
    print(f'Foram informados {len(num)} valores ao todo')
    mai = 0
    for pos, n in enumerate(num):
        if pos == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'O maior valor informado foi {mai}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

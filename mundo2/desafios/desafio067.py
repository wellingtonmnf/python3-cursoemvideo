while True:
    n = int(input('Quer ver a tabuada de qual valor? (n < 0 encerra): '))
    print('-' * 50)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
        break
    else:
        c = 1
        while c <= 10:
            print(f'{n:3} x {c:2} = {(n*c):4}')
            c += 1
        print('-' * 50)

from random import randint

numcomp = randint(0,10)
#print(numcomp)
tentativas = 0
numjog = int(input('Digite um número entre 1 e 10: '))

if numjog == numcomp:
    tentativas += 1
    print(f'PARABÉNS! Você acertou! Você fez {tentativas} tentativa!')
else:
    tentativas += 1
    while numjog != numcomp:
        print(f'Você errou! Tente novamente!')
        numjog = int(input('Digite um número entre 1 e 10: '))
        tentativas += 1
    print(f'PARABÉNS! Você acertou! Você fez {tentativas} tentativas!')
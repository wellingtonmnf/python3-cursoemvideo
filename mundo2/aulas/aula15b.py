n = cont = s = 0
# Repetição com flag
'''while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1'''
# Repetição com flag
'''while n != 999:
    n = int(input('Digite um número: '))
    s += n
print(f'A soma vale {s}')'''
# Repetição com looping infinito
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

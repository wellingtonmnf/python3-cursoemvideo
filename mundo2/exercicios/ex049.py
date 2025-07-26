num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{num:3} x {c:2} = {(num * c):3}')

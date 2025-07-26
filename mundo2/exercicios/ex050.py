soma, cont = 0, 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número (inteiro): '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número(s) par(es) e a soma dele(s) é igual a {soma}')

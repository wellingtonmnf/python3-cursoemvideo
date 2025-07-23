print('Digite três números para serem analisados')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
maior = 0
menor = 0

if n1 == n2 and n2 == n3:
    print('O números são iguais')
else:
    # Checagem do maior número
    if n1 >= n2 and n1 >= n3:
        maior = n1
    if n2 >= n1 and n2 >= n3:
        maior = n2
    if n3 >= n1 and n3 >= n2:
        maior = n3
    # Checagem do menor número
    if n1 <= n2 and n1 <= n3:
        menor = n1
    if n2 <= n1 and n2 <= n3:
        menor = n2
    if n3 <= n1 and n3 <= n2:
        menor = n3

    print(f'O \033[7;34mmaior\033[m número é {maior}')
    print(f'O \033[7;33mmenor\033[m número é {menor}')

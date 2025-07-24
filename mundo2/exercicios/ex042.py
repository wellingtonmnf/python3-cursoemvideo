a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo ', end='')

    if a == b == c:
        print('equilátero')
    elif a != b != c != a: #Precisa comparar novamente o último com o primeiro. SENÃO DÁ ERRO!
        print('escaleno')
    else:
        print('isósceles')

else:
    print('Os segmentos NÃO podem formar um triângulo')

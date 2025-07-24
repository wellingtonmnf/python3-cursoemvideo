print('^' * 27)
print('CLASSIFICADOR DE TRIÂNGULOS')
print('^' * 27)

print('Vamos checar se é possível fazer um triângulo...')
print('Informe as medidas dos lados:')
a = float(input('LADO A: '))
b = float(input('LADO B: '))
c = float(input('LADO C: '))

print(f'Medidas: A = {a:.2f} | B = {b:.2f} | C = {c:.2f}')

if a < b + c and b < a + c and c < a + b:
    print('É possível fazer um triângulo com essas medidas? R: \033[7:32mSIM\033[m')

    if a == b and b == c:
        print('Este será um triângulo \033[7;33mEQUILÁTERO\033[m')
    elif a != b and b != c:
        print('Este será um triângulo \033[7;35mESCALENO\033[m')
    else:
        print('Este será um triângulo \033[7;34mISÓSCELES\033[m')

else:
    print('É possível fazer um triângulo com essas medidas? R: \033[7:31mNÃO\033[m')
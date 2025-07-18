from math import sqrt

ctop = float(input('Digite o cateto oposto: '))
ctad = float(input('Digite o cateto adjacente: '))
hpqd = pow(ctop, 2) + pow(ctad, 2)
print(f'O valor da hipotenusa é = {sqrt(hpqd):.2f}')
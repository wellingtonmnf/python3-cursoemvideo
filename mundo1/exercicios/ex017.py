from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co**2 + ca**2) ** (1/2)
hi = hypot(co, ca)
print('A hipotenusa é igual a {:.2f} (sem importação de módulo)'.format(h))
print('A hipotenusa é igual a {:.2f} (com importação de módulo)'.format(hi))
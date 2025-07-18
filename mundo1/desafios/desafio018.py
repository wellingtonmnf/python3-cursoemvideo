from math import radians, sin, cos, tan

a = float(input('Digite o valor do ângulo: '))
r = radians(a)
print(f'Ângulo = {a:.2f}º | Seno = {sin(r):.2f}º | Cosseno = {cos(r):.2f}º | Tangente = {tan(r):.2f}º')
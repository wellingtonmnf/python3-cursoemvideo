import math

ang = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)

print(f'| Ângulo: {ang:.2f}º | Radiano: {rad:.3f} rad | Seno: {sen:.3f}º | Cosseno: {cos:.3f}º | Tangente: {tg:.3f}º |')
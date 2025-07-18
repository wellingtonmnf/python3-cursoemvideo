l = float(input('Largura da parede (m): '))
h = float(input('Altura da parede (m): '))
a = l*h
print(f'Sua parede possui {l:.2f} m de largura x {h:.2f} m de altura,\ncom uma área total de {a:.2f} m².')
print(f'Para pintar essa parede, você precisará de:\n * {(a*0.5):.2f} l de tinta para 1 demão;\n * {(a*1):.2f} l de tinta para 2 demãos;\n * {(a*1.5):.2f} l de tinta para 3 demãos;')
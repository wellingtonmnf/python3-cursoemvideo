l = float(input('Digite a largura da parede (m): '))
h = float(input('Digite a altura da parede (m): '))
a = l*h
print(f'Para uma parede com {a:>5.2f}m², serão necessários: \n * {(a/2):>6.2f} litros de tinta para pintá-la com 1 demão; \n * {a:>6.2f} litros de tinta para pintá-la com 2 demãos; \n * {(a*1.5):>6.2f} litros de tinta para pintá-la com 3 demãos;')
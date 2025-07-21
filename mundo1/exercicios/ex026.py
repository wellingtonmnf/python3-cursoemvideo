f = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {f.count('A')} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {f.find('A') + 1}.')
print(f'A última letra "A" aparece na posição {f.rfind('A') + 1}.')

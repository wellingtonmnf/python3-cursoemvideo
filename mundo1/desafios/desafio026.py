frase = str.strip(input('Digite uma frase: '))
frase = frase.upper()
print(f'A letra "A" aparece {frase.count('A')} vezes na frase. A 1ª vez é na posição {frase.find('A')} e a última vez é na posição {frase.rfind('A')}')
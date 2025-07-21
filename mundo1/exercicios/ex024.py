cidade = str(input('Digite o nome da cidade: ')).strip()
print(f'O nome da cidade começa com a palavra "SANTO?" -> R: {'SANTO' in cidade[:5].upper()}')
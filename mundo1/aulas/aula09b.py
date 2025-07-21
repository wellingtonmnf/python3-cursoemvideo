frase = '   Curso em Vídeo Python  '

print(frase)
print(frase.count('o')) # conta quantas vezes o caractere 'o' (minúsculo) aparece dentro da string
print(frase.count('o',0,13)) # conta quantas vezes o caractere 'o' (minúsculo) aparece dentro da string, da posição 0 até a 13ª posição da string
print(frase.count('O')) # conta quantas vezes o caractere 'O' (maiúsculo) aparece dentro da string
print(frase.upper().count('O')) # coloca todas as letras da string em maúsculo e conta quantas vezes o caractere 'O' (maiúsculo) aparece dentro da string
print(len(frase)) # conta quantas posições existem no vetor da string
print(len(frase.strip())) # poda todos os caracteres vazios no início e no fim da string conta quantas posições existem no vetor da string
print(len(frase.rstrip())) # poda todos os caracteres vazios no fim (direita) da string conta quantas posições existem no vetor da string
print(len(frase.lstrip())) # poda todos os caracteres vazios no início (esquerda) da string conta quantas posições existem no vetor da string
frase = frase.replace('Python','Java') # substitui trechos de uma string
print(frase)
print(len(frase))
# frase[0] = 'J' # Esse código gera erro, pois uma string é imutável
print('Curso' in frase) # Mostra se a string está contida no vetor de string
print(frase.find('Curso')) # Mostra a posição em que string está contida no vetor de string, caso exista
print(frase.find('Vídeo')) # Mostra a posição em que string está contida no vetor de string, caso exista
print(frase.find('video')) # Mostra a posição -1, pois a string não está contida no vetor de string, logo não exista
print(frase.lower().find('vídeo')) # Converte a string para letras minúsculas e mostra a posição -1, pois a string não está contida no vetor de string, logo não exista
print(frase.split()) # Cria uma lista dividindo o vetor de strings em strings menores, separadas por espaço
dividido = frase.split()
print(dividido[0]) # Mostra o primeiro item da lista
print(dividido[2][3]) # Mostra a posição 3 da string na posição 2 da lista

def funcao():
    n1 = 4 # Variável LOCAL com o mesmo nome
    print(f'N1 dentro vale {n1}')


n1 = 2 # Variável GLOBAL que NÃO É AFETADA pela manipulação da variável local de mesmo nome
funcao()
print(f'N1 fora vale {n1}')

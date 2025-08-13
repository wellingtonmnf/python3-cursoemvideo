# Escopo de variáveis
def teste():
    x = 8 # Variável de escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2 # Variável de escopo global
print(f'No programa principal, n vale {n}') # Funciona em todo o programa, incuíndo nas funções
print(f'No programa principal, x vale {x}') # Dará erro, pois seu ciclo de vida está apenas dentro da execução da função
teste()

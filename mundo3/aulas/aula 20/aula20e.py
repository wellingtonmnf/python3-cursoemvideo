def contador(* num): # O símbolo de * na frente do argumento serve para empacotar os parâmetros de uma função
    print(num) # O retorno do empacotamento se dá como uma tupla com todos os valores passados
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

# Com isso, é possível passar um número indeterminado de argumentos como parâmetros para uma função
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

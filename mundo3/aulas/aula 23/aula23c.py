try: # Tenta executar um bloco de código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))  # Caso seja 0, retorna exceção (ZeroDivisionError)
    r = a / b
except Exception as erro: # Executa caso haja exceção, captur a exceção e joga em uma variável
    print(f'Problema encontrado foi: {erro.__class__}') # Exibe a classe do tipo de exceção
else: # Executa caso não haja exceção (opcional)
      print(f'O resultado é {r:.1f}')
finally: # Executa independente do resultado do processamento anterior (opcional)
    print('Volte sempre! Muito obrigado!')
    
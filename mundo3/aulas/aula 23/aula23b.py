try: # Tenta executar um bloco de código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))  # Caso seja 0, retorna exceção (ZeroDivisionError)
    r = a / b
except: # Executa caso haja exceção
    print('Infelizmente tivemos um problema :(')
else: # Executa caso não haja exceção (opcional)
      print(f'O resultado é {r:.1f}')
finally: # Executa independente do resultado do processamento anterior (opcional)
    print('Volte sempre! Muito obrigado!')

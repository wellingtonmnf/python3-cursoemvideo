try: # Tenta executar um bloco de código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))  # Caso seja 0, retorna exceção (ZeroDivisionError)
    r = a / b
except (ValueError, TypeError): # Executa caso haja exceção dos tipos definidos
    print(f'Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: # Caso haja interrupção do programa
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # Executa caso não haja exceção (opcional)
      print(f'O resultado é {r:.1f}')
finally: # Executa independente do resultado do processamento anterior (opcional)
    print('Volte sempre! Muito obrigado!')
    
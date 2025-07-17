# Pedindo um valor ao usuário
var = input('Digite algo: ')
# Checando o valor na variável
print('Tipo do dado digitado:', type(var))
# Checando todas as informações possíveis sobre o valor na variável
print('Este valor é numérico? ', var.isnumeric())
print('Este valor é alfabético? ', var.isalpha())
print('Este valor é alfanumérico? ', var.isalnum())
print('Este valor é composto só de letras maiúsculas? ', var.isupper())
print('Este valor é composto só de letras minúsculas? ', var.islower())
print('Este valor é numérico decimal? ', var.isdecimal())
print('Este valor é um dígito? ', var.isdigit())
print('Este valor é uma string vazia? ', var.isspace())
print('Este valor é imprimível? ', var.isprintable())
print('Este valor é uma palavra reservada? ', var.isidentifier())
print('Este valor está na tabela ASCII? ', var.isascii())
print('Este valor é um título? ', var.istitle())

# Pedindo um valor ao usuário
var = input('Digite algo: ')
# Checando o valor na variável
print('Tipo do dado digitado:', type(var))
# Checando todas as informações possíveis sobre o valor na variável
print('Este valor contém apenas letras? ', var.isalpha())
print('Este valor contém apenas caracteres alfanuméricos? ', var.isalnum())
print('Este valor contém apenas numéros decimais? ', var.isdecimal())
print('Este valor contém apenas dígitos? ', var.isdigit())
print('Este valor contém apenas caracteres numéricos? ', var.isnumeric())
print('Este valor contém apenas caracteres maiúsculas? ', var.isupper())
print('Este valor contém apenas caracteres minúsculas? ', var.islower())
print('Este valor contém apenas termos capitalizados? ', var.istitle())
print('Este valor contém apenas espaços em branco? ', var.isspace())
print('Este valor contém apenas caracteres imprimíveis? ', var.isprintable())
print('Este valor contém apenas caracteres da tabela ASCII? ', var.isascii())
print('Este valor pode ser usado como nome de variável? ', var.isidentifier())

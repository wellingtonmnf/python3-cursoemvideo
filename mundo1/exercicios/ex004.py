value = input('Digite algo: ')
print('Tipo primitivo do valor: ', type(value))
print(f'Só tem espaços? {value.isspace()}')
print('É um número? {}'.format(value.isnumeric()))
print('É alfabético? ', value.isalpha())
print('É alfanúmerico? ', value.isalnum())
print(f'Está em maiúsculas? {value.isupper()}')
print('Está em minúsculas? {}'.format(value.islower()))
print('Está capitalizada?', value.istitle())
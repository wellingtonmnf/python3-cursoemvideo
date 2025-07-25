print('=' * 20)
print(f'{"CHECA-PALÍNDROMO":=^20}')
print('=' * 20)

frase = str(input('Digite a frase: ')).upper().strip().split()
seq = ''
inv = ''

for c in range(0, len(frase)):
    seq += frase[c]
print(f'{"Sequência de caracteres (original):":<37} {seq}')

for c in range(len(seq) - 1, -1, -1):
    inv += seq[c]
print(f'{"Sequência de caracteres (invertidos):":<37} {inv}')

if seq == inv:
    print('A FRASE É UM PALÍNDROMO?: R: \033[7;32mSIM\033[m')
else:
    print('A FRASE É UM PALÍNDROMO? R: \033[7;31mNÃO\033[m')

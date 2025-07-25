print('-' * 26)
print('NÚMEROS \033[7;34mPARES\033[m ENTRE 1 E 50')
print('-' * 26)

for c in range(0, 51):
    if c % 2 == 0:
        print(f'{c} ', end='')

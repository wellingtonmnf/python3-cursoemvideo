from time import sleep
import emoji

print('*' * 32)
print('CONTAGEM REGRESSIVA DE REVEILLON')
print('*' * 32)

for c in range(10, -1, -1):
    sleep(1)
    print(f'{c}...', end='')
print('FELIZ ANO NOVO!!! ', end='')

for c in range(0, 5):
    print(emoji.emojize(':fireworks::sparkler:'), end='')

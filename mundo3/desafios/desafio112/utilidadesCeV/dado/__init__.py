def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).strip()

        convertido = False

        if (len(valor) > 0
                and (valor.count(',') + valor.count('.')) <= 1
                and valor.count(' ') == 0):

            invalidos = 0
            for v in valor:
                if v.isalpha() or v in '+-*/=&$#@?!': # Aumentar essa lista de caracteres para aumentar o critério de validação
                    invalidos += 1

            if invalidos == 0 and valor != ',' and valor != '.':
                convertido = True

        print(valor)

        if convertido:
            valor = valor.replace(',', '.')
            return float(valor)
        else:
            print(f'\033[31mERRO! "{valor}" é um preço inválido!.\033[m')

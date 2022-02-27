def remover_caracteres(cnpj):
    # 04.252.011/0001-10 > 04252011000110
    cnpj = list(cnpj)
    del (cnpj[2:11:4])
    cnpj.pop(12)
    cnpj = [str(i) for i in cnpj]
    cnpj = ''.join(cnpj)
    return cnpj


def validacao(cnpj):
    # Retorna o CNPJ completo
    cnpj = [int(i) for i in cnpj[:-2]]
    cnpj = primeiro_digito(cnpj)
    cnpj = segundo_digito(cnpj)
    cnpj = [str(i) for i in cnpj]
    cnpj = ''.join(cnpj)
    return cnpj


def primeiro_digito(cnpj):
    # Acrescenta o 1º Digito: 042520110001X
    multiplicador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    resultado = 11 - (sum([cnpj[i] * multiplicador[i] for i in range(len(cnpj))]) % 11)
    if not resultado > 9:
        cnpj.append(resultado)
    else:
        cnpj.append(0)
    return cnpj


def segundo_digito(cnpj):
    # Acrescenta o 1º Digito: 0425201100011X
    multiplicador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    resultado = 11 - (sum([cnpj[i] * multiplicador[i] for i in range(len(cnpj))]) % 11)
    if not resultado > 9:
        cnpj.append(resultado)
    else:
        cnpj.append(0)
    return cnpj


while True:
    cnpj = input('Insira o CNPJ: ')
    if len(cnpj) == 18:
        cnpj = remover_caracteres(cnpj)

    if len(cnpj) == 14:
        cnpj_validado = validacao(cnpj)
        if cnpj == cnpj_validado:
            print('\nCNPJ informado é válido!\n')
        else:
            print('\nCNPJ informado é inválido!\n')
    else:
        print('\nCNPJ INVALIDO\n')
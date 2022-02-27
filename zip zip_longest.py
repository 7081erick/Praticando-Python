from itertools import zip_longest, count

indice = count()
cidade = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']
estados = ['SP', 'MG', 'BA', ]
cidades_estados = zip(indice, cidade, estados)

for indice, estados, cidade in cidades_estados:
    print(indice,estados, cidade)
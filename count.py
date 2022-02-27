"""
count - Itertools
"""
from itertools import count

contador = count(0,10)
lista = ['Erick', 'João', 'Ana']
for valor in contador:
    print(valor)

    if valor == 100:
        break

lista = zip(contador, lista)
print(list(lista))
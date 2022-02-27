"""

Combinatios, Permutations e Product = Itertools
Combinação - Ordem não importa
Permutação - ordem importa
Ambos não repetem valores únicos
Produto - ordem importa e repete valores únicos
"""
from itertools import permutations, combinations, product

pessoa = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in product(pessoa, pessoa):
    print(grupo)



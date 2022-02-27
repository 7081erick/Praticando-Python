"""
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v *2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['luiz', 'mauro', 'maria']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)

"""
# list = [1, 2, 'a', 3.14]
# list_comprehension = [(expressão) for (nome da nova função) in (funçao), for loop apenas True ]

# square = []
# for i in range(1,101):
#     square.append(i**2)
# print(square)
# #######
# square2 = [(i**2) for i in range(1, 101)]
# print(square2)
# remainders5 = [x**2 % 5 for x in range(1, 101)]
# print(remainders5)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)
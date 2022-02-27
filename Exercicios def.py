##### Exercicio 1 #####
# def comeco (saudacao= 'Bem vindo', nome=input('Escreva seu nome: ')):
#     return f'{nome}, {saudacao}'
# variavel = comeco()
# print(variavel)

##### Exercicio 2 #####
# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
# soma(1+2+3)

# ##### Exercicio 3 #####
# def aumento(valor, percentual):
#     return(valor + (valor * percentual/100))
#
# ap = aumento(50,10)
# print(ap)

##### Exercicio 4 #####
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisivel por 3 e 5'
    if n % 3 == 0:
        return f'Fizz, {n} é divisivel por 3'
    if n % 5 == 0:
        return f'Buzz, {n} é divisivel por 5'
    return n
from random import randint

for i in range(100):
    aleatorio = randint(1,100)
    print(fb(aleatorio))




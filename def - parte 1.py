"""
Funções - def em Python (Parte 1)
"""

def saudacao(msg='oi', nome='usuario'):
    nome = nome.replace('u', '8')
    msg = msg.replace('o', '0')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
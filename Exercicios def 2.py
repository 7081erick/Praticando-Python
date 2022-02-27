
def func(nome, saudacao):
    nome = 'Erick'
    saudacao = ', Bem vindo'
    return nome + saudacao

def func2(arg):
    return arg

#func()
variavel = func2(arg=func(nome='',saudacao=''))

print(variavel)
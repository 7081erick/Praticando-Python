# No dicionario eu controlo o index/chave enquanto na lista o index é dado

# d1 = dict(chave1 = 'valor da chave', chave2='valor da outra chave')
# d1['nova_chave'] = 'valor da nova chave'
# print(d1, type(d1))
#

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome':'Otavio',
    },
    'cliente2' : {
            'nome' : 'erick',
            'sobrenome' : 'michael',
    },
}
a = ('gay')
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f' {dados_k} = {dados_v}')
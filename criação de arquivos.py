"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendos linhas: ')
print(file.read())

file.close()
#######################################
with open('abc.txt', 'w+') as file:
    file.write('Linha')
    file.seek(0)
    print(file.read())
    file.close()

"""
import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade' : '20',
    },
    'Pessoa 2':{
        'nome': 'Erick',
        'idade': '30',
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
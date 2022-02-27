print('Vc é bem gay')
print()
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b', }
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das opções abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv ['resposta_certa']:
        print('Parabéns')
        respostas_certas += 1
    else:
        print('Errou')
    print()

quantidade_pergunta = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_pergunta * 100
porcentagem_acerto = int(porcentagem_acerto)
print(f'Você acertou {quantidade_pergunta}/{len(perguntas)}')
print(f'Você acertou: {porcentagem_acerto}%')


def func(*args, **kwargs):
    print(args)

    idade =kwargs.get('idade')
    if idade is not None:
        print(f'Sua idade é: {idade}')



lista = [1,2,3,4,5]
func(*lista, 6, idade=30)

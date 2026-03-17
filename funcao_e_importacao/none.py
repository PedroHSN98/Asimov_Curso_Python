produtos = {
    'banana' : 3.60,
    'leite' : 4.60,
    'carne': 15.65,
    'pão': 2.77,
}

print(produtos.get('banana'))
print(produtos.get('pão'))
print(produtos.get('arroz'))

def dizer_ola():
    print('Olá')

retorno = dizer_ola()
print(retorno)
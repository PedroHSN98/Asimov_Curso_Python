#nome = 'Gabriel'

#for caracter in nome:
#    print(f'Cada letra se encontra aqui: {caracter}')'''

clientes = [
    ('Fernando', 'xxx', 'xxx@hotmail.com'), 
    ('Gabriel', 'yyy', 'yyy@gmail.com')
    ]

for cliente in clientes:
# for nome, cpf, email in clientes:
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]
    #nome, cpf, email = cliente
    print(f'Nome: {nome}\nCPF: {cpf}\nE-mail:{email}\n\n')

print('Acabou o loop')

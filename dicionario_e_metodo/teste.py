dicionario = {}

dicionario [27] = 'Pedro'
dicionario ['jogador'] = True
dicionario ['@gmail.com'] = 12


for di in dicionario:
    valor = dicionario[di]
    print(f'O valor: {valor} e as chaves: {di}')
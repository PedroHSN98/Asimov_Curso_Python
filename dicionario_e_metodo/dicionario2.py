d = {}

d[10] = 'abc'
d['CHAVE'] = 5
d[3.15] = True

print(d)

for k in d:
    v = d[k]
    print(f'Chave: {k}, Valor: {v}')
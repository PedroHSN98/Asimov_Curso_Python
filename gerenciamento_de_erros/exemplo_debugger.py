nomes = ['Jose', 'Gustavo', 'Augusto', 'Fernando']
#idades = [10, 20, 30, 40]
idades = [18, 16, 18, 49]

for nome, idade in zip(nomes, idades):
    if idade >= 18: #tirando o '=' ira ter erro
        maior_de_idade = True
    elif idade < 18:
        maior_de_idade = False
    print(f'{nome} tem {idade} anos. É maior de idade? {maior_de_idade}')
from pathlib import Path

#Lendo um arquivo forma não recomendada
'''
pasta_atual = Path(__file__).parent

lista_compras = open(pasta_atual / 'lista_de_compras.txt')
print(lista_compras.read())
lista_compras.close()
'''

'''
#Lendo arquivo forma recomendada
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r') as lista_de_compras:
    print(lista_de_compras.read())
'''

'''
#lendo linha a linha
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r') as lista_de_compras:
    linha = lista_de_compras.readline()
    while linha != '':
        print(linha)
        linha = lista_de_compras.readline()
'''      
'''
#lendo todas as linhas
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r') as lista_de_compras:
    print(lista_de_compras.readlines())
'''
'''
#escrevendo arquivos
pasta_atual = Path(__file__).parent
itens_ja_comprados = ['leite', 'pao', 'queijo']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizadas:
    for item in itens_lista:    
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizadas.write(item)
'''


#escrevendo linha a linha 
pasta_atual = Path(__file__).parent
itens_ja_comprados = ['leite', 'pao', 'queijo']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:    
    if not item.replace('\n', '') in itens_ja_comprados:
        itens_lista_atualizada.append(item)

with open('lista_de_compras_atualizada.txt', mode='w') as lista_atualizadas:
    lista_atualizadas.writelines(itens_lista_atualizada)   

print(itens_lista_atualizada)


#Acrescentando valores a um arquivo

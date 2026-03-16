# Dados Duas listas, printe todas os valores que aparecem
#duplicados nas duas listas

valores1 = [1, 5, 7, 9, 12]
valores2 = [2, 4, 7, 10, 12]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f'Valor {valor1} aparece nas duas listas')

# Dado duas listas, printe uma mensagem dizendo se existe
#algum elemento em comum entre elas ou não.

lista1 = [10.0, 'xx', True]
lista2 = [00.10, False, 'xxx']

elemento_em_comum = False

for valor1 in lista1:
    if elemento_em_comum:
        break
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_em_comum = True,
            break

if elemento_em_comum:
    print(f'As listas {lista1} e {lista2} possuem elementos em comum')
else:
    print(f'As listas {lista1} e {lista2} não possuem elementos em comum')



#Dado uma sequencia de números, calcule a soma e media dos números.
#ATENÇÃO: não vale usar a função sum()!

#dado uma sequencia de numeros, calcule o maior valor da sequencia.
#Atenção: não vale usar a função max()!

#Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres

soma = 0

for seq in range(0,21):
    soma += seq
    media = soma / 20

print(f'Aqui está a soma total: {soma}')
print(f'Aqui está a media de todos os números: {media}\n')

#dado uma sequencia de numeros, calcule o maior valor da sequencia.
#Atenção: não vale usar a função max()!

numeros = [16, 32, 65, 23, 87]
maior_valor = numeros[0]

for num in numeros:
    if num > maior_valor:
        maior_valor = num
print(f"O maior valor da sequência é: {maior_valor}\n")




#Dado uma lista de palavras, printe todas as palavras
palavras = ['bola', 'banana', 'brinquedo', 'faca', 'sol']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Aqui estão as palavras que possuiem mais de 5: {palavra}')
# Crie um código que implementa a "Cifra de César", isto é , que 
#Transforma uma string movendo cada letra um cenrto numero de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

#Exemplo:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
#"Cachorro" com chave -1 = "Bzbgnqqn"
#"Ola Mundo!" com chave 3 = "Roá Pxgr!"

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    #Lidar com situação onde indice esta a direita da seq

    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

texto = 'ABCDE'
chave = 2

cifra = ''

for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maiusculas:
        caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)





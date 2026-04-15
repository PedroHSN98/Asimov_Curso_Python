#cada chave é a palavra em letras minusculas,
#e cada valor associado é um número de caracteres da palavra, se contar espaços em branco

#Exemplo de lista de palavras e o dicionario resultante:

palavras = ['Ólá', 'Python', 'Juliano', 'Asimov Academy']


dict_caracteres = {
    palavra.lower(): len(palavra.replace (' ', ''))
    for palavra in palavras
}

print(dict_caracteres)


'''
dict_caracteres = {
    'olá': 3,
    'python': 6,
    'juliano': 7,
    'asimov academy': 13,
}
'''

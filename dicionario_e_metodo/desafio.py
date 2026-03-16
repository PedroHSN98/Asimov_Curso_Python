#Crie um código que conta o número de vogais de um bloco de texto
#qualquer. O código deve desconsiderar letras maiúscilals/minusculas
#isto é 'a' e 'A' contem da mesma forma.
# O texto pode ser colado diretamente como um string no codigo

texto = '''Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython.'''

vogais = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0,
}

for caractere in texto:
    if caractere.upper() == 'A':
        vogais['A'] += 1
    if caractere.upper() == 'E':
        vogais['E'] += 1
    if caractere.upper() == 'I':
        vogais['I'] += 1
    if caractere.upper() == 'O':
        vogais['O'] += 1
    if caractere.upper() == 'U':
        vogais['U'] += 1

for vogal, contagem in vogais.items():
    print(f'Há {contagem} letras {vogal} no texto.')


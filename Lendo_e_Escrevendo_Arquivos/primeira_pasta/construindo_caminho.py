from pathlib import Path

caminho = Path('primeira_pasta/segunda_pasta')
#caminho = Path('primeira_pasta') / 'segunda_pasta'

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)




print(caminho)
print(type(caminho))
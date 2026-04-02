from pathlib import Path
import os

#Retorna o caminho do diretorio de trabalho atual
print(Path.cwd())

#Esse caminho é absoluto
print(Path.cwd().is_absolute())

#Retornando caminho da primeira pasta
print(Path('primeira_pasta'))

#Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())

#transformando o caminho em absoluto
print(Path.cwd() / Path('primeira_pasta'))
print((Path.cwd() / 'primeira_pasta').exists()) #verificando se o caminho existe

os.chdir(Path.home()) 
print(Path.cwd() / Path('primeira_pasta'))
print((Path.cwd() / 'primeira_pasta').exists())

print(__file__) #caminho do arquivo atual
print(Path(__file__).is_absolute()) #verificando se o caminho é absoluto
print(Path(__file__).parent) #caminho do diretorio pai
print(Path(__file__).parent / 'primeira_pasta') #caminho do diretorio pai + pasta
print((Path(__file__).parent / 'primeira_pasta').exists())#verificando se o caminho existe

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)
print(caminho_arquivo.parent.parent.parent)
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)

print(caminho_arquivo.parents[1])
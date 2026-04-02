from pathlib import Path
import os

#Listando arquivos de uma pasta
#print(os.listdir(Path.cwd()))
#print(list(Path.cwd().glob('*'))) #Listando arquivos com extensão

#Listando arquivos de uma determinada extensão
#print(list(Path.cwd().glob('*.py')))


#Listar tudo dentro de uma pasta
#print(list(Path.cwd().glob('**/*')))
#print(list(Path.cwd().glob('**/*.txt'))) pegar tudos arquivos de texto dentro da pasta e subpastas


#Validando caminhos
nao_existe = Path() / 'não_existe'
print(nao_existe.exists()) #verificando se o caminho existe



#verificando se é arquivo ou pasta
print(Path(__file__))
print(Path(__file__).is_file())
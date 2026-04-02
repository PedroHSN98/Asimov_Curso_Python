import pickle
from pathlib import Path
pasta_atual = Path(__file__).parent


#Salvando arquivo Pickle
minha_lista = [1, 2, 3, 4, 5]
meu_dict = {'nome': 'Adriano', 'idade': 30, 'cidade': 'Porto Alegre'}

'''
with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'wb') as f:
    pickle.dump(minha_lista, f)

with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'wb') as f:
    pickle.dump(meu_dict, f)

#lendo arquivo pickle
with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'rb') as f:
    minha_lista_lida = pickle.load(f)
with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'rb') as f:
    minha_dict_lida = pickle.load(f)

print(type(minha_lista_lida))
print(minha_dict_lida)
'''

#salvando a instancia de uma classe com pickle
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def quem_sou_eu(self):
        print(f'Eu sou {self.nome} e tenho {self.idade} anos.')

inst_joao = Pessoa('João', 25)
inst_joao.quem_sou_eu()

with open(pasta_atual / 'pickles' / 'inst_joao.pickle', 'wb') as f:
    pickle.dump(inst_joao, f)


#lendo a mesma instancia

with open(pasta_atual / 'pickles' / 'inst_joao.pickle', 'rb') as f:
    inst_joao_lida = pickle.load(f)

inst_joao_lida.quem_sou_eu()
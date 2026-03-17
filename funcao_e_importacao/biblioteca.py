
#https://docs.python.org/pt-br/3.6/library/index.html

import math
print(math.pi)
print(math.log(16, 2))

import datetime
print(datetime.datetime.now())
agora = datetime.datetime.now()

ano_2000 = datetime.datetime(2000, 1, 1)
print(agora - ano_2000)

import random
for _ in range(5):
    n = random.randint(1, 10)
    print(f'Número escolhido: {n}')

nomes = ['Juliano', 'Marcos', 'Paulo']

for no in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')

import os

print(os.getcwd())
print(os.listdir())


import time 

inicio = time.time()

print('Primeira Linha')
time.sleep(3)
print('Segunda Linha')

final = time.time()

tempo_execucao = final - inicio
print(f'O Script levou {tempo_execucao:.2f} segundos para ser executado')

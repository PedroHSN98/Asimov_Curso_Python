#Desafio 3
#Meus amigos possuem os seguinte interesses:

#Gostam de programação: Ricardo, Roberto, Pedro, Vinicius
#Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinicius
#Estudam na Asimov Academy: Ricardo, Mateus, Paulo, Pedro

#Unsando operações de conjunto, encontra o conjunto
#de amigos que gostam de programação e estudam na Asimov Academy, mas que não gostam de jogar futebol.

programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
asimov_academy = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}
interesse_comum = (programacao & asimov_academy) - futebol
print(interesse_comum)
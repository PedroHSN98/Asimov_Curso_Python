#Desafio - Crie um programa que :
# Pede pelo seu nome e idade
# da oi para você 
# conta quantas letras tem o seu nome
#fala quantos anos voce tera daqui 5 anos 

nome = str(input('Qual é o seu nome: '))
idade = int(input('Quantos anos você tem: '))

print(f'Olá {nome}, é  bom ter você aqui com a gente')

soma_nome = len(nome)
print(f'Está é a quantidade de letras que tem o seu nome: {soma_nome}')

soma_cinco = (idade + 5)
print(f'Você tera uma idade de {soma_cinco}   anos daqui 5 anos')
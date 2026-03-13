# Desafio - Crie um programa que:
# - Escolhe um numero secreto.
# - Pede por um chute do usuario
# - Indica se o usuario acertou ou não
# - Se não acertou, da uma dica, dizendo 
# - se o número é mais alto ou mais baixo 
# - repete isso até 3 vezes!

numero_secreto = 10
descobriu = False


for n in range(3):
    if not descobriu:
        chute = int(input('Digite o seu número secreto: '))
        if chute < numero_secreto:
            print('Chute muito Baixo')
        elif chute > numero_secreto:
                print('Chute foi Muito Grande')
        else:
            print('Descobriu')
            descobriu = True

if descobriu:
    print('PRABÉNS, VOCÊ GANHOU!')
else:
    print(f'Que pena, voce perdeu!, não temos mais tentativas, o resultado era: {numero_secreto} ')




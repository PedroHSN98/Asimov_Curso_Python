# Desafio - Crie um programa que:
# - Escolhe um número secreto
# - Pede por um chute do usuario
# - Indica se o usuario acertou ou não
# - Se não acertou, da uma dica, dizendo
# - se o número é mais alto ou mais baixo
# - repete isso até 3 vezes!

numero_secreto = 10
descobriu = False

if not descobriu:
    chute = int(input('Digite o número que você acha que é: '))
    if chute < numero_secreto:
        print('Chute muito Baixo')
    elif chute > numero_secreto:
        print('Chute muito alto')
    else:
        print('Descobriu')
        descobriu = True

if not descobriu:
    chute = int(input('Digite o número que você acha que é: '))
    if chute < numero_secreto:
        print('Chute muito Baixo')
    elif chute > numero_secreto:
        print('Chute muito alto')
    else:
        print('Descobriu')
        descobriu = True

if not descobriu:
    chute = int(input('Digite o número que você acha que é: '))
    if chute < numero_secreto:
        print('Chute muito Baixo')
    elif chute > numero_secreto:
        print('Chute muito alto')
    else:
        print('Descobriu')
        desscobriu = True


if descobriu == True or numero_secreto == chute:
    print('Parabéns Você achou o número aleatorio')
else:
    print('Que pena você errou e perdeu as tentativas')


            

    



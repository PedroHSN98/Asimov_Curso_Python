# Desafio - Crie um programa que:
# - Escolhe um número secreto
# - Pede por um chute do usuario
# - Indica se o usuario acertou ou não
# - Se não acertou, da uma dica, dizendo
# - se o número é mais alto ou mais baixo
# - repete isso até 3 vezes!

numero_secreto = 10

for i in range(3):
    chute = int(input('Digite o Numero Aleatorio:'))

    if chute == numero_secreto:
        print('Parabéns Você Achou o numero secreto')
        break
    elif chute < numero_secreto:
        print('O numero é muito menor')
    elif chute > numero_secreto:
        print('O numero é muito maior')

else:
    print(f'Suas tentativas chegaram ao limite. O número secreto é :{numero_secreto}')
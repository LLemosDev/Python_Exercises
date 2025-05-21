# Pedra Papel Tesoura

from random import randint

print('Escolha uma opção: \n'
      '[ 0 ] Pedra\n'
      '[ 1 ] Papel\n'
      '[ 2 ] Tesoura')

jogador = int(input("Qual sua jogada? "))
computador = randint(0, 2)

if jogador == 0 and computador == 1:
    print("Você escolheu Pedra e o computador Papel, você perdeu!")
elif jogador == 0 and computador == 2:
    print("Você escolheu Pedra e o Computador Tesoura, você ganhou!")
elif jogador == 0 and computador == 0:
    print("Você escolheu Pedra e o computador Pedra, empate!")
elif jogador == 1 and computador == 0:
    print("Você escolheu Papel e o computador Pedra, você ganhou!")
elif jogador == 1 and computador == 2:
    print("Você escolheu Papel e o computador Tesoura, você perdeu!")
elif jogador == 1 and computador == 1:
    print("Você escolheu Papel e o computador Papel, empate!")
elif jogador == 2 and computador == 0:
    print("Você escolheu Tesoura e o computador Pedra, você perdeu!")
elif jogador == 2 and computador == 1:
    print("Você escolheu Tesoura e o computador Papel, você ganhou!")
elif jogador == 2 and computador == 2:
    print("Você escolheu Tesoura e o computador Tesoura, empate!")
else:
    print("Digite uma opção válida")

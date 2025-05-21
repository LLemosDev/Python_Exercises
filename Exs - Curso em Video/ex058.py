# Jogo da Adivinhação 2.0

from random import randint

tentativas = 1
num = randint(0, 10)

print("==" * 5, "Jogo da Adivinhação 2.0", "==" * 5, "\nVou pensar em um número de 0 a 10\nTente Acertar!")
escolha = int(input("Sua escolha: "))

while escolha != num:
    if escolha > num:
        escolha = int(input("Menos... Tente novamente\nSua escolha: "))
        tentativas += 1
    else:
        escolha = int(input("Mais... Tente novamente\nSua escolha: "))
        tentativas += 1

print("Acertou com %d tentativas. Parabéns!" % tentativas)
# Jogo da adivinhação

import random
from time import sleep

print("-=-" * 25)
print('\033[34mJogo da Adivinhação, Vou pensar em um número de 0 a 5, tente adivinhar!\033[m')
print("-=-" * 25)

numeros = [0, 1, 2, 3, 4, 5]
numero_correto = random.choice(numeros)

numero_chute = int(input("Tente Adivinhar em qual número estou pensando: "))

print('\033[36mPROCESSANDO...')
sleep(2)

if numero_correto == numero_chute:
    print("\033[32mVocê Acertou!")
else:
    print(f"\033[31mVocê Errou!, o número que eu estava pensando era o {numero_correto}")




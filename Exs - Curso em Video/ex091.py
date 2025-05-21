# Jogo de Dados com Dicionário

from time import sleep
from random import randint

jogadores = {}

for i in range(4):
    jogadores[f'jogador{i + 1}'] = randint(1, 6)
    print(f"O jogador{i + 1} tirou {jogadores[f'jogador{i + 1}']}")
    sleep(1)

ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

print('==RANKING DOS JOGADORES==')

for indice, valor in enumerate(ranking):
    print(f"{indice + 1}º lugar: {valor[0]} com {valor[1]} pontos")
    sleep(1)




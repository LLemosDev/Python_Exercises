# Criador de jogos para MegaSena

from random import randint

jogos = []
cont = 0
numero_jogos = int(input('Quantos jogos deseja sortear: '))

print("-=" * 3 + f"  SORTEANDO {numero_jogos} JOGOS  " + "-=" * 3 )
for i in range(numero_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo)

for n, j in enumerate(jogos):
    print(f"Jogo {n + 1}: {j}")

print("-=" * 5 + " < BOA SORTE > " + "-=" * 5)





# Cadastro jogador de Futebol

jogador = {'nome': input('Nome: ')}
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
gols = []

for i in range(partidas):
    gol = int(input(f'Quantos gols {jogador['nome']} fez na partida {i + 1}: '))
    gols.append(gol)

jogador['gols'] = gols
jogador['total'] = sum(gols)

# 1 forma de exibição
print(jogador)

print("-=" * 30)

# 2 forma de exibição
for chave, valor in jogador.items():
    print(f"O campo {chave} tem valor {valor}")

print("-=" * 30)
# 3 forma de exibição
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for i, v in enumerate(jogador['gols']):
    print(f"Na {i + 1}ª partida, fez {v} gols")




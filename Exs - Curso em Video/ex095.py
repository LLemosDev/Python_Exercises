# Aprimorando Dicionários

jogadores = []

while True:
    jogador = {'nome': input('Nome: ')}
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    gols = []

    for i in range(partidas):
        gol = int(input(f'Quantos gols {jogador['nome']} fez na partida {i + 1}: '))
        gols.append(gol)

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador)

    resposta = input('Deseja continuar [S/N]: ').strip().upper()
    while resposta not in "SN":
        resposta = input('Deseja continuar [S/N]: ').strip().upper()

    if resposta == "N":
        break

print(f"{"cod":<3} {"NOME":^8} {"GOLS":>12} {"TOTAL":>8}")
print("-=" * 20)

for i, v in enumerate(jogadores):
    print(f"{i:<3} {v['nome']:^10} {str(v['gols']):>15} {v['total']:>5}")

print("-=" * 20)
while True:
    analisar = int(input('Digite o cod do jogador que deseja analisar (999 interrompe): '))

    if analisar == 999:
        print("PROGRAMA ENCERRADO")
        break

    elif analisar < len(jogadores) and analisar > -1:
        print(f"Jogador {jogadores[analisar]['nome']}:")
        for i, v in enumerate(jogadores[analisar]['gols']):
            print(f"Na {i + 1}ª partida, fez {v} gols")

    else:
        print("Insira um código válido")
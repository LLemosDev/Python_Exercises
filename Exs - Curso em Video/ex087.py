# Matriz 3x3 com analise de dados

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        ponto = int(input(f'Digite o valor para [{l}, {c}]: '))
        if ponto % 2 == 0:
            soma += ponto
        matriz[l][c] = ponto

print("-=" * 30)

for linha in matriz:
    print(f"[{linha[0]:^5}] [{linha[1]:^5}] [{linha[2]:^5}]")

print("-=" * 30)

soma_coluna3 = sum(matriz[l][2] for l in range(3))
print(f"A soma de todos os valores pares digitados é {soma}\n"
      f"A soma dos valores da 3ª coluna é {soma_coluna3}\n"
      f"O maior valor da 2ª linha é {max(matriz[1])}")

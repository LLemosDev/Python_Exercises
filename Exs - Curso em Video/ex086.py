# Matriz 3x3

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(len(matriz)):
    for i in range(len(matriz[l])):
        ponto = int(input(f'Digite um valor para [{l}, {i}]: '))
        matriz[l][i] = ponto

print("-=" * 30)
for linha in matriz:
        print(f"[{linha[0]:^5}] [{linha[1]:^5}] [{linha[2]:^5}]")



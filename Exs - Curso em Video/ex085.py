# Lista com Pares e ímpares

numeros = [[], []]

for i in range(0, 7):
    valor = int(input(f"Digite o {i + 1} valor: "))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort(); numeros[1].sort()

print(f"Os valores parss digitados foram: {numeros[0]}\n"
      f"OS valores ímpares digitados foram: {numeros[1]} ")


# Lista ordenada sem repetições

numeros = []

for i in range(0, 5):
    numero = int(input('Digite um valor: '))

    if i == 0:
        numeros.append(numero)
        print("Adicionado ao final da lista...")
    elif numero > numeros[-1]:
        numeros.append(numero)
        print("Adicionado ao final da lista...")
    elif numero in numeros:
        print("Valor duplicado, não será adicionado.")
    else:
        pos = 0
        while pos < len(numeros):
            if numero < numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
        print(f"Valor adicionado na posição {pos}")

print(numeros)  




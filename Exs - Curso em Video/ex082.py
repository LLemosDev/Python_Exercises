# Dividindo valores em várias listas

numeros = []
pares = []
impares = []

while True:

    numero = int(input('Digite um número: '))
    numeros.append(numero)
    resposta = input('Deseja continuar? [S/N]: ').strip()

    if resposta in "Nn":
        break

for i, n in enumerate(numeros):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
print(f"Lista completa {numeros}\n"
      f"Lista de pares {pares}\n"
      f"Lista de ímpares {impares}")
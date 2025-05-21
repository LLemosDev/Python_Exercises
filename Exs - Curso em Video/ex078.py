# Maior e menor valores na lista

li = []

for i in range(0, 4):
    li.append(int(input(f'Digite um valor para posição {i}: ')))

maior = max(li)
menor = min(li)

print("Você digitou os valores: ", li)
print(f"O maior valor digitado foi {maior}, encontrado na(s) posição: ", end="")

for x in range(0, len(li)):
    if li[x] == maior:
        print(x, "...", end="")

print(f"\nO menor valor digitado foi {menor}, encontrado na(s) posição: ", end="")

for x in range(0, len(li)):
    if li[x] == menor:
        print(x, "...", end="")
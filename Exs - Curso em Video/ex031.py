# Viagem

d = float(input("Digite a distancia da viagem em KM: "))

if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45

print(f"Sua viagem de {d}Km teve o preço de passagem de R${preco}")
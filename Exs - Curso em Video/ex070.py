# Estatísticas em Produto

print("_" * 20)
print("  LOJÃO DO JORJÃO")
print("_" * 20)

total = 0
preco_barato = 0
produto_barato = None
p1000 = 0


while True:
    produto = input("Nome do produto: ")
    preco = float(input("Digite o valor de produto: "))

    # Assume que o primeiro produto é o mais barato, pois é a primeira iteração do loop
    if total == 0:
        preco_barato = preco
        produto_barato = produto

    total += preco

    if preco > 1000:
        p1000 += 1

    if preco < preco_barato:
        preco_barato = preco
        produto_barato = produto

    escolha = input('Quer continuar [S/N] ?').strip().upper()
    if escolha == "N":
        break

    while escolha != "S" and "N":
        escolha = input('Quer continuar [S/N] ?').strip().upper()


print(f"O total da compra foi de R${total}\n"
      f"Temos {p1000} produtos custanto mais de R$1000\n"
      f"O produto mais barato foi {produto_barato}")

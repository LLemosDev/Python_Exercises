listagem = ('Lápis', 1.5, 'Caneta', 2.5, 'Caderno', 20, 'Estojo', 10,
            'Borracha', 1.5, 'Apontador', 2, 'Régua', 9, 'Lapiseira', 5)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<30}", end="")
    else:
        print(f"R${listagem[i]}")
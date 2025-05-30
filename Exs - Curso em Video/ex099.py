# Função que descobre o maior

def maior(*num):
    if len(num) == 0:
        print("Nenhum parâmetro foi dado")
    else:
        maior = max(num)
        print("Analisando os valores passados...")
        print(*num)
        print(f"Ao todo foram informados {len(num)} números\nO maior número foi {maior}")
        print("-=" * 30)

maior(2,3, 4, 5, 6, 10, 45, 8, 9)
maior(3, 5, 1, -5, 20, 56, 2)
maior(1, 2)
maior()
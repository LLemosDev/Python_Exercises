# Função calcula área

def area(l, c):
    a = l * c
    print(f"A área do terreno de {l}x{c} é de {round(a, 2)}m²")


print("Controle de Terrenos")
print("-" * 25)

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)

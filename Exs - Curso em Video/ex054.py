# Grupo de Maioridade

pessoas = []
grupo_maior =[]
grupo_menor = []

for i in range(1, 8):
    pessoa = int(input(f"Em que ano a {i} pessoa nasceu? "))
    pessoas.append(pessoa)

    if 2025 - pessoa > 18:   # [i - 1] para pegar todos os indices, pois i no laço, começa com valor = 1
        grupo_maior.append(pessoa)
    else:
        grupo_menor.append(pessoa)


print(f"Ao todo tivemos {len(grupo_maior)} pessoas maiores de idade\nE {len(grupo_menor)} pessoas menores de idade")
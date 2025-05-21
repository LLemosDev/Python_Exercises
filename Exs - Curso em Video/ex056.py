# Analisador Completo
# O código lê o nome, idade e sexo de 4 pessoas e retorna a média de idade do grupo, o nome do
# homem mais velho, e sua idade, e por fim quantas mulheres tem menos que 20 anos, retornando seu nome e idade

soma_idade = 0
pessoas = []
idade_homem_velho = 0
homem_velho = 0
mulheres20 = 0

for p in range(1, 5):
    print(f"____ {p}ª PESSOA____")
    pessoa = {
    "nome" : input("Nome: ").strip(),
    "idade": int(input("Idade: ")),
    "sexo" : input("Sexo (M/F): ").upper().strip()
    }
    pessoas.append(pessoa)
    soma_idade += pessoa["idade"]

    if pessoa["sexo"] == "M" and pessoa["idade"] > idade_homem_velho:
        homem_velho = pessoa["nome"]
        idade_homem_velho = pessoa["idade"]

    if pessoa["sexo"] == "F" and pessoa["idade"] < 20:
        mulheres20 += 1

media_idade = soma_idade/4
print(f"A média de idade do grupo é de {round(media_idade, 2)}"
      f"\nO homem mais velho é {homem_velho} com {idade_homem_velho} anos"
      f"\nE no grupo temos {mulheres20} mulher(es) com menos de 20 anos")




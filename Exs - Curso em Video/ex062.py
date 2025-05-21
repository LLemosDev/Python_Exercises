# Progressão Aritmética V - 3.0

primeiro = int(input("Digite o valor do primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for i in range(10):
    print(primeiro, "-> ", end="")
    primeiro += razao
print("PAUSA")

termos = int(input("Quantos termos você deseja mostrar a mais: "))
cont = termos

while termos != 0:
    for x in range(termos):
        print(primeiro, "-> ", end="")
        primeiro += razao
    print("PAUSA")
    termos = int(input("Quantos termos você deseja mostrar a mais: "))
    cont += termos

print("A Progressão foi finalizada com %d termos" % (cont + 10))
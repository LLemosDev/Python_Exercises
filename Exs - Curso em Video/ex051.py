# 10 primeiros termos de uma PA (Progressão Aritmética)

termo1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo1 + (11 - 1) * razao

for i in range(termo1, decimo, razao):
    print(i, end = ' -> ')
print("ACABOU")
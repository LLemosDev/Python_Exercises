# Analisando e Classificando Triangulos

a = int(input('Digite o valor do primeiro segmento: '))
b = int(input('Digite o valor do segundo segmento: '))
c = int(input('Digite o valor do terceiro segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) and (b == c):
        print("Os segmentos podem formar um triângulo EQUILÁTERO")
    elif (a != b) and (b != c) and (a != c):
        print("Os segmentos podem formar um triângulo ESCALENO")
    else:
        print("Os segmentos podem formar um triângulo ISÓSCELES")
else:
    print("Os segmentos não podem formar um triângulo")
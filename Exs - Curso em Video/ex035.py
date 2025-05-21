# Analisando Triangulo

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os segmentos podem formar um triângulo")
else:
    print("Os segmentos não podem formar um triângulo")
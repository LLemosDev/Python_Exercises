# Calculadora de IMC

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso/altura**2

if imc < 18.5:
    print(f"IMC = {round(imc, 2)}, Abaixo do peso")
elif imc < 25:
    print(f"IMC = {round(imc, 2)}, Peso ideal")
elif imc < 30:
    print(f"IMC = {round(imc, 2)}, Sobrepeso")
elif imc < 40:
    print(f"IMC = {round(imc, 2)}, Obesidade")
else:
    print(f"IMC = {round(imc, 2)}, Obesidade Mórbida")
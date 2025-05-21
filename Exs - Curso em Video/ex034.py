# Aumento de Salário

s = float(input("Qual o seu salário? "))
a = None

if s > 1250:
    a = (s * 10)/100
else:
    a = (s * 15)/100

print(f"Seu salrário de R${s} será aumentado para R${s + a}")
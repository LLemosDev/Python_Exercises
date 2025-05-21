# Simulador de Caixa eletrônico

print("=-=" * 9 + "\n     CAIXA ELETRÔNICO\n" + "=-=" * 9)
saque = int(input('Digite o valor que você quer sacar: '))
total = saque

nota50 = saque // 50
saque %= 50

nota20 = saque // 20
saque %= 20

nota10 = saque // 10
saque %= 10

nota1 = saque

print(f"Você sacou R${total} e recebeu:\n"
      f"{nota50} notas de 50\n"
      f"{nota20} notas de 20\n"
      f"{nota10} notas de 10\n"
      f"{nota1} notas de 1")





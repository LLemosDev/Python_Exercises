# Gerenciador de Pagamamentos

valor = float(input('Digite o valor da compra: '))
print('Como deseja pagar:\n'
      '[ 1 ] à vista - dinheiro/cheque\n'
      '[ 2 ] à vista - cartão\n'
      '[ 3 ] 2x - cartão\n'
      '[ 4 ] 3x ou mais - cartão')

option = int(input('Digite uma opção: '))

if option == 1:
    vf = valor - (valor * 10)/100
    print(f"A compra de R${valor}, sendo paga à vista no dinheiro/cheque, sai num valor final de {round(vf, 2)}")
elif option == 2:
    vf = valor - (valor * 5)/100
    print(f"A compra de R${valor}, sendo paga à vista no cartão, sai num valor final de {round(vf, 2)}")
elif option == 3:
    vf = valor
    print(f"A compra de R${valor}, sendo paga em 2x no cartão, sai num valor final de {round(vf, 2)}")
else:
    vf = valor + (valor * 20)/100
    print(f"A compra de R${valor}, sendo paga em 3x ou mais no cartão, sai num valor final de {round(vf, 2)}")


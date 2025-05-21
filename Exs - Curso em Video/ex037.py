# Conversor de Bases

num = int(input('Digite um número inteiro: '))

print("Escolha uma das bases para conversão:"
      "\n[ 1 ] BINARIO"
      "\n[ 2 ] OCTAL"
      "\n[ 3 ] HEXADECIMAL")

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f"O número {num} convertido em Binário é igual a {bin(num)}")
elif opcao == 2:
    print(f"O número {num} convertido em Octal é igual a {oct(num)}")
elif opcao == 3:
    print(f"O número {num} convertido em Hexadecimal é igual a {hex(num)}")
else:
    print("Opção digitada não é válida")
# Menu de Opções Básicas

from time import sleep

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

valores = [valor1, valor2]
valores.sort()


while True:
    print("==" * 10, "\n"
            "[ 1 ] somar\n"
            "[ 2 ] multiplicar\n"
            "[ 3 ] subtrair\n"
            "[ 4 ] maior\n"
            "[ 5 ] novos numeros\n"
            "[ 6 ] fechar programa\n",
            "==" * 10, "")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
        sleep(2)
    elif opcao == 2:
        print(f"{valor1} X {valor2} = {valor1 * valor2}")
        sleep(2)
    elif opcao == 3:
        print(f"{valor1} - {valor2} = {valor1 - valor2}")
        sleep(2)
    elif opcao == 4:
        print(f"{valores[1]} > {valores[0]}")
        sleep(2)
    elif opcao == 5:
        print("Digite os novos valores: ")
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        sleep(2)
    elif opcao == 6:
        print("Programa encerrado")
        break
    else:
        opcao = int(input("Digite uma opção válida: "))





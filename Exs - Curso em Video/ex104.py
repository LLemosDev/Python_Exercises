# validando entrada de dados

def leiaInt():
    while True:
        num = input('Digite um numero: ')
        if num.isnumeric():
            print(f"Você acabou de digitar o número {num}")
            break
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")

leiaInt()

# Alistamento Militar


nascimento = int(input('Digite o ano de nascimento: '))
situacao = 2025 - nascimento
print(f"Quem nasceu em {nascimento} tem {2025 - nascimento} anos em 2025")

if situacao == 18:
    print("Você deve se alistar Imediatamente")
elif situacao < 18:
    print(f"Você ainda vai se alistar daqui {18 - situacao} anos\nSeu alistamento será em {2025 + (18 - situacao)}")
else:
    print(f"Você já deveria ter se alistado há {-1 * (18 - situacao)} anos\nOu você já se alistou em {2025 + (18 - situacao)}")
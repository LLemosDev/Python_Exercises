# Clasisificando Atletas

nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = 2025 - nascimento

if idade <= 9:
    print(f"O atleta que nasceu no ano {nascimento}, tem {idade} anos e é classificado como \033[32mMIRIM")
elif idade <= 14:
    print(f"O atleta que nasceu no ano {nascimento}, tem {idade} anos e é classificado como \033[35mINFANTIL")
elif idade <= 19:
    print(f"O atleta que nasceu no ano {nascimento}, tem {idade} anos e é classificado como \033[34mJUNIOR")
elif idade <= 25:
    print(f"O atleta que nasceu no ano {nascimento}, tem {idade} anos e é classificado como \033[33mSÊNIOR")
else:
    print(f"O atleta que nasceu no ano {nascimento}, tem {idade} anos e é classificado como \033[31mMASTER")
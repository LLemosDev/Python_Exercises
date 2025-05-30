# Função voto

def voto(ano_nascimento):
    print("_" * 30)
    idade = 2025 - ano_nascimento

    if idade < 16:
        print(f"com {idade} anos: NÃO VOTA")
    elif 16 <= idade < 18 or idade > 65:
        print(f"com {idade} anos: VOTO OPCIONAL")
    else:
        print(f"com {idade} anos: VOTO OBRIGATÓRIO")

ano = int(input("Em qual você nasceu? "))
voto(ano)
# Sistema interativo de ajuda em Python

def pyHelp(comando):
        print("-=" * 30)
        print(f"Acessando o manual do comando '{comando}'")
        print("-=" * 30)

        return help(comando)

        print("Sistema de ajuda PyHELP")
        print("-=" * 30)


while True:
    print("-=" * 15)
    print("SISTEMA DE AJUDA PyHelp")
    print("-=" * 15)
    comando = input("Função ou Biblioteca > ")
    if comando == "fim".strip().lower():
        print("Programa encerrado")
        break
    pyHelp(comando)

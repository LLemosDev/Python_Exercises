# Analisando grupo de dados

grupo_maior = 0
homens = 0
mulheres20 = 0

while True:
    print("CADASTRE UMA PESSOA")
    idade = int(input("idade: "))
    sexo = input("sexo [M/F]: ").strip().upper()

    if idade > 18:
        grupo_maior += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1

    continua = input("Deseja continuar [S/N]: ").upper().strip()
    if continua == "N":
        break

print(f"Ao todo temos {grupo_maior} pessoas com mais de 18 anos é\n"
      f"Ao todo temos {homens} homens cadastrados\n"
      f"Ao todo temos {mulheres20} mulheres com menos de 20 anos")
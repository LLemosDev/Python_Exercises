# Boletim com lista composta
alunos = []

while True:
    aluno = []
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    aluno.append(nome); aluno.append(nota1); aluno.append(nota2)
    alunos.append(aluno)

    resposta = input('Deseja continuar [S/N]? ').strip()

    if resposta in "Nn":
        break

print("-=" * 20)

print(f"{"No.":<4} {"NOME":^10} {"MÉDIA":>8}")
print("-" * 25)

# Loop para exibir todos os alunos com suas médias
for i, a in enumerate(alunos):
    media = (a[1] + a[2])/2
    print(f"{i:<4} {a[0]:^10} {media:>8.2f}")

while True:
    verificar = int(input('Deseja acessar as notas de qual aluno (999 para): '))

    if verificar == 999:
        break

    elif verificar < len(alunos):
        print(f"Notas de {alunos[verificar][0]}:\n"
              f"Nota 1: {alunos[verificar][1]}\nNota 2: {alunos[verificar][2]}")

    else:
        print("Insira um número válido")


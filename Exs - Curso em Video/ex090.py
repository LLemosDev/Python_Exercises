# Dicionário em Python

aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a média de {aluno['nome']}: '))

print(f"Aluno: {aluno['nome']}\n"
      f"Média: {aluno['media']}")

if aluno['media'] >= 7:
    print("Situação: \033[32mAprovado")
elif aluno['media'] >= 5:
    print("Situação: \033[34mRecuperação")
else:
    print("Situação: \033[31mReprovado")
# Cadastro de Trabalhador em Python
from datetime import datetime

trabalhador = {}


trabalhador['nome'] = input('Digite o nome: ')
trabalhador['ano_nascimento'] = int(input('Digite o ano de nascimento: '))
trabalhador['carteira_trabalho'] = int(input('Digite a carteira de trabalho (0 não tem): '))
trabalhador['idade'] = datetime.now().year - trabalhador['ano_nascimento']

if trabalhador['carteira_trabalho'] != 0:
    trabalhador['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    trabalhador['salario'] = float(input('Digite o valor do salário: '))
    trabalhador['aposentadoria'] = ((trabalhador['ano_contratacao'] + 35) - datetime.now().year) + trabalhador['idade']

for chave, valor in trabalhador.items():
    print(f"{chave}: {valor}")

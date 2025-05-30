#  Analisando e gerando Dicionários

def notas(*notas, sit=False):
    """
    --> Função para analisar notas de alunos e dizer a situação da turma
    :param notas: uma ou mais notas de alunos
    :param sit: opcional, mostra a situação da turma
    :return: dicionário com informações da turma
    """

    turma = {}
    turma['quantidade de notas'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['média'] = round(sum(notas)/len(notas), 2)

    if sit:
        if turma['média'] < 6:
            turma['situação'] = "RUIM"
        elif turma['média'] >= 6 and turma['média'] < 7.5:
            turma['situação'] = "RAZOAVEL"
        else:
            turma['situação'] = "BOA"

    return turma

resp = notas(1.5, 4.5, 10, 6.5)
print(resp)

help(notas)

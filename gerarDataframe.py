import pandas as pd
import json

# Algumas configurações para exibir o DataFrame no console
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.width', 200)
pd.set_option('expand_frame_repr', True)


# Função para ler um arquivo JSON contendo o Nome, idade, curso e semestre do aluno
def importdata():
    with open('alunos.json', encoding='utf-8') as alunos:
        dados = json.load(alunos)

    alunos = pd.json_normalize(dados,
                               meta=['nome', ['idade', 'curso', 'semestre']])

    alunos.columns = ["Nome", "Idade", "Curso", "Semestre"]

    alunos["Dados"] = "Idade: " + alunos["Idade"].astype(str) + "; Curso: " + alunos["Curso"].astype(
        str) + "; Semestre: " + alunos["Semestre"].astype(str)

    return alunos

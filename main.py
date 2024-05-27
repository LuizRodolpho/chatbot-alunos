import google.generativeai as genai
import numpy as np
import gerarDataframe

# Cria um DataFrame Pandas
df_alunos = gerarDataframe.importdata()

# Ativando a API do Google usando a API key
GOOGLE_API_KEY = "SUA_API"
genai.configure(api_key=GOOGLE_API_KEY)

# Configurando os parâmetros do chatbot
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

# Dando instruções sobre como será o comportamento do chatbot
system_instruction = ("Você é um assistente de uma escola que dá informações para os alunos nos corredores"
                      "Você fala igual um estudante, porém sem muitas gírias e com respostas razoavelmente curtas")

# Selecionando o modelo para fazer o embedding do DataFrame de Alunos
model = 'models/embedding-001'


# Função para criar o Embedding de um título(aluno) com texto(informações do aluno)
def embed_fn(title, text):
    return genai.embed_content(model=model,
                               content=text,
                               title=title,
                               task_type="RETRIEVAL_DOCUMENT")["embedding"]


print("Gerando embeddings, aguarde...")

# Usando uma função lambda para criar um Embedding para cada aluno
df_alunos["Embeddings"] = df_alunos.apply(lambda row: embed_fn(row["Nome"], row["Dados"]), axis=1)


# Função para ler uma consulta, criar um Embedding da consulta, e compará-la com o Embedding mais próximo do DataFrame
def gerar_consulta(consulta):
    embedding_consulta = genai.embed_content(model=model,
                                             content=consulta,
                                             task_type="RETRIEVAL_QUERY")

    produtos_escalares = np.dot(np.stack(df_alunos["Embeddings"]), embedding_consulta["embedding"])

    indice = np.argmax(produtos_escalares)
    return df_alunos.iloc[indice]["Dados"]


# Ler uma pergunta
consulta = input("Me pergunte algo sobre qualquer aluno: ")

# Ler e responder uma pergunta enquanto a pegunta seja diferente de "" (vazio)
while consulta != "":

    trecho = gerar_consulta(consulta)

    # Algumas instruções sobre como o chatbot irá responder à pergunta (semelhante ao feito na linha '27')
    prompt = (f"Você é um assistente de uma faculdade. Responda essa pergunta {consulta}."
              f" Usando como base essa informação {trecho}."
              f" Caso a pergunta não tenha nada a ver com Nome, Curso, Idade, ou Semestre cursado você responde algo"
              f" como 'Vixi! vou ficar devendo essa, mais alguma coisa?' Você naõ responde nada a mais, exceto sobre "
              f"Nome, Curso, Idade, ou Semestre cursado."
              f" Se a pergunta não tiver contexto com a informação dada, você responde o que foi feito na pergunta."
              f" Depois de responder pergunte se a pessoa quer saber algo mais sobre a faculdade?")

    # Criando um modelo generativo
    modelo2 = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    safety_settings=safety_settings,
                                    system_instruction=system_instruction
                                    )

    response = modelo2.generate_content(prompt)

    print(response.text)

    consulta = input()

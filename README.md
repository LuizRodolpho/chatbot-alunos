# Chatbot de Assistência de Alunos
Este programa usa um chatbot para interpretar dados de alunos de um arquivo JSON. Oferece informações detalhadas, como nome, idade e curso, por meio de interações com o usuário.

# Recursos:
**Leitura de Arquivos JSON:** O programa é capaz de ler arquivos JSON contendo informações dos alunos de forma eficiente.  
**Interpretação de Dados:** O chatbot interpreta os dados dos alunos e fornece respostas precisas e relevantes às perguntas do usuário.  
**Respostas Personalizadas:** O chatbot oferece respostas personalizadas com base nas consultas dos usuários, garantindo uma experiência interativa e informativa.  
**Facilidade de Uso:** O código é simples e bem documentado, facilitando a compreensão e a personalização para diferentes necessidades.  

# Como Usar:
1. Extraia todos os arquivos para uma **mesma pasta** que **não** contenha nenhum outro arquivo.
2. Você precisa ter o Python instalado no seu computador, você pode instalar aqui: https://www.python.org/downloads/
3. Editar o arquivo **main.py** usando uma **IDE** (sugiro PyCharm Community Edition [Baixe aqui](https://www.jetbrains.com/pycharm/download/?section=windows)) ou algum **Python Notebook** (Como o Google Colab)
4. Você irá precisar de uma API Key do Gemini, você pode ver como ativar a sua em https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br  
5. Coloque sua **API do Google** na **linha 9** onde está escrito **SUA_API**  
6. Instale as bibliotecas **pandas**, **numpy** e **google.generativeai** usando os seguintes códigos um de cada vez no terminal da IDE utilizada:  
  pip install pandas  
  pip install numpy  
  pip install google-generativeai  
7. **Verifique** se o arquivo **alunos.json** se localiza na **mesma pasta dos arquivo chatbot e gerarDataframe**  
8. Executar o arquivo main.py  

# Observação:
  Ao fazer várias perguntas consecutivas, o programa pode retornar o erro: **"google.api_core.exceptions.ResourceExhausted: 429 Resource has been exhausted (e.g. check quota)."**  
  Caso isso aconteça, apenas espere um pouco e rode o programa novamente.

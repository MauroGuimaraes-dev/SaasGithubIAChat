# Importa a biblioteca Streamlit para criar a interface web
import streamlit as st
# Importa a biblioteca os para manipular variáveis de ambiente
import os
# Importa a classe App do Embedchain para processar e consultar dados
from embedchain import App
# Importa load_dotenv para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria um cabeçalho na barra lateral para configuração das APIs
st.sidebar.header("⚙️ Configuração das APIs")

# Cria um campo de entrada para a chave da API OpenAI na barra lateral
openai_key_input = st.sidebar.text_input("Insira sua chave de API da OpenAI", type="password")
# Se uma chave OpenAI foi fornecida, define ela como variável de ambiente
if openai_key_input:
    os.environ["OPENAI_API_KEY"] = openai_key_input

# Cria um campo de entrada para o token do GitHub na barra lateral
github_token_input = st.sidebar.text_input("Insira seu Token do GitHub", type="password")
# Se um token GitHub foi fornecido, define ele como variável de ambiente
if github_token_input:
    os.environ["GITHUB_TOKEN"] = github_token_input

# Cria um botão para registrar as APIs na barra lateral
if st.sidebar.button("Registrar APIs"):
    if openai_key_input and github_token_input:
        st.session_state['bot'] = App()
        st.sidebar.success("APIs registradas com sucesso!")
    else:
        st.sidebar.error("Por favor, insira ambas as chaves de API.")

# Define o estilo CSS para o título com largura total
st.markdown("""
    <style>
        .title-container {
            background-color: #000080;
            padding: 20px;
            margin: -20px -400px 20px -400px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
            width: calc(100% + 800px);
        }
        .title-text {
            color: white;
            font-size: 48px;
            font-weight: bold;
            text-shadow: 0 0 10px #fff, 
                         0 0 20px #fff, 
                         0 0 30px #e60073, 
                         0 0 40px #e60073;
            margin: 0;
            padding: 0;
        }
        .subtitle-text {
            color: white;
            font-size: 20px;
            margin-top: 10px;
            text-shadow: 0 0 5px #fff;
        }
    </style>
    <div class="title-container">
        <h1 class="title-text">SaaS - GitHub AI Chat</h1>
        <p class="subtitle-text">Desenvolvido por Mauro de Souza Guimarães</p>
    </div>
""", unsafe_allow_html=True)

# Adiciona instruções na barra lateral
st.sidebar.title("📖 Instruções de Uso")

# Instruções para a API da OpenAI
st.sidebar.header("🔑 Como obter a API Key da OpenAI")
st.sidebar.markdown("""
1. Acesse [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Faça login ou crie uma conta
3. Clique em "Create new secret key"
4. Copie a chave gerada e cole abaixo
""")

# Instruções para o Token do GitHub
st.sidebar.header("🔒 Como gerar o Token do GitHub")
st.sidebar.markdown("""
1. Acesse [GitHub Tokens](https://github.com/settings/tokens)
2. Clique em "Generate new token (classic)"
3. Dê um nome ao token (ex: "AI Chat Access")
4. Selecione os seguintes escopos:
   - ✓ `repo` (acesso completo)
   - ✓ `read:org`
   - ✓ `read:user`
5. Defina a expiração (recomendado: 30 dias)
6. Clique em "Generate token"
7. **IMPORTANTE**: Copie o token gerado imediatamente
   (ele não será mostrado novamente!)
""")

# Instruções de uso do aplicativo
st.sidebar.header("🚀 Como usar o aplicativo")
st.sidebar.markdown("""
1. Insira suas chaves de API abaixo
2. Clique em "Registrar APIs"
3. Cole o endereço do repositório no formato:
   `usuário/repositório`
4. Clique em "Registrar URL"
5. Faça suas perguntas sobre o repositório!
""")

# Inicializa o bot na sessão se ainda não existir
if 'bot' not in st.session_state:
    st.session_state['bot'] = App()

# Cria um cabeçalho para a seção de consulta do GitHub
st.header("Consultar Repositório GitHub")
# Cria um campo de entrada para o endereço do repositório GitHub
github_url_input = st.text_input("Insira o endereço do GitHub (usuário/repositório)")
# Cria um botão para registrar a URL do repositório
if st.button("Registrar URL"):
    # Verifica se todos os dados necessários foram fornecidos
    if github_url_input and github_token_input and 'bot' in st.session_state:
        try:
            # Constrói a URL completa do GitHub
            github_url = f"https://github.com/{github_url_input}"
            # Adiciona o conteúdo do repositório ao bot como texto
            st.session_state['bot'].add(github_url, data_type="text")
            # Mostra mensagem de sucesso
            st.success(f"URL {github_url} registrada com sucesso!")
        except Exception as e:
            # Mostra mensagem de erro se algo der errado
            st.error(f"Erro ao registrar URL: {str(e)}")
    else:
        # Mostra mensagem de erro se algum dado estiver faltando
        st.error("Por favor, insira o endereço do GitHub e configure as APIs primeiro.")

# Cria um cabeçalho para a seção de perguntas
st.header("Faça uma pergunta sobre o repositório")
# Cria uma área de texto para inserir a pergunta
user_question = st.text_area("Digite sua pergunta aqui")
# Cria um botão para enviar a pergunta
if st.button("Enviar"):
    # Verifica se há uma pergunta e se o bot está inicializado
    if user_question and 'bot' in st.session_state:
        try:
            # Obtém a resposta do bot para a pergunta
            response = st.session_state['bot'].query(user_question)
            # Mostra a resposta em uma área de texto
            st.text_area("Resposta", response, height=200)
        except Exception as e:
            # Mostra mensagem de erro se algo der errado
            st.error(f"Erro ao processar a pergunta: {str(e)}")
    else:
        # Mostra mensagem de erro se faltar pergunta ou bot
        st.error("Por favor, registre um repositório GitHub antes de fazer perguntas.")

# Verifica se o arquivo .env existe
if not os.path.exists('.env'):
    # Se não existir, cria o arquivo .env com as chaves
    with open('.env', 'w') as f:
        # Escreve a chave da API OpenAI
        f.write(f"OPENAI_API_KEY={openai_key_input}\n")
        # Escreve o token do GitHub
        f.write(f"GITHUB_TOKEN={github_token_input}\n")

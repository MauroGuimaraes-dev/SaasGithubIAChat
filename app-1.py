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

# Define o título principal da aplicação
st.title("GitHub AI Chat")
# Adiciona uma linha de texto com o nome do desenvolvedor
st.write("Desenvolvido por Mauro de Souza Guimarães")

# Cria um cabeçalho na barra lateral para configuração das APIs
st.sidebar.header("Configuração das APIs")

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
    # Verifica se ambas as chaves foram fornecidas
    if openai_key_input and github_token_input:
        # Cria uma nova instância do bot e armazena na sessão
        st.session_state['bot'] = App()
        # Mostra mensagem de sucesso
        st.sidebar.success("APIs registradas com sucesso!")
    else:
        # Mostra mensagem de erro se alguma chave estiver faltando
        st.sidebar.error("Por favor, insira ambas as chaves de API.")

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

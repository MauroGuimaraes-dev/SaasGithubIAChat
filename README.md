# SaaS - GitHub AI Chat 🚀

Bem-vindo ao **SaaS - GitHub AI Chat**! Este aplicativo permite que você faça perguntas sobre o conteúdo de um repositório GitHub usando a tecnologia de geração aumentada por recuperação (RAG).

## 🛠️ Tecnologias Utilizadas

- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) - Interface gráfica
- ![Embedchain](https://img.shields.io/badge/Embedchain-4B8BBE?style=for-the-badge&logo=python&logoColor=white) - Integração com GitHub e OpenAI
- ![Python-dotenv](https://img.shields.io/badge/Python--dotenv-FFD43B?style=for-the-badge&logo=python&logoColor=blue) - Gerenciamento de variáveis de ambiente

## 📦 Instalação

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure suas chaves de API:**
   - Crie um arquivo `.env` na raiz do projeto e adicione suas chaves:
     ```text
     OPENAI_API_KEY=sua-chave-da-openai-aqui
     GITHUB_TOKEN=seu-token-do-github-aqui
     ```

## 🚀 Como Executar

Para iniciar o aplicativo, execute o seguinte comando: 

Acesse o aplicativo em seu navegador através do endereço: `http://localhost:8501`

## 🌐 Deploy

Para fazer o deploy do aplicativo, você pode usar plataformas como Heroku, AWS, ou Streamlit Sharing. Aqui está um exemplo de como fazer o deploy no Streamlit Sharing:

1. **Faça login no [Streamlit Sharing](https://streamlit.io/sharing)**
2. **Conecte seu repositório GitHub**
3. **Configure as variáveis de ambiente no painel de configurações**
4. **Clique em "Deploy"**

## 🤝 Contribuição

Sinta-se à vontade para contribuir com este projeto. Para isso, siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça o commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça o push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por Mauro de Souza Guimarães
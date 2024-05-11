# Image-to-Text-to-Audio

Uma ferramenta com IA que transforma imagem para texto com uma descrição do ambiente e por fim transforma para áudio..

A ferramenta utiliza o modelo GEMINI-PRO-VISION para a transformação da imagem para texto

![](https://github.com/Henriquerezer/Image-to-Text-to-Audio/assets/87787728/7d2e3b65-b2d3-4471-adc4-2df30f8fa69d)
![](https://github.com/Henriquerezer/Alura-gemini-week/assets/87787728/823fe438-ba1b-4790-ad7a-59c8bbed6127)

## Configuração do Ambiente

### Pré-requisitos
- Python 3.8+

# requirements

- os
- dotenv
- transformers
- langchain
- requests
- streamlit
- google.generativeai

### Configuração das Chaves de API
Adicione suas chaves de API ao arquivo .env na raiz do projeto:
```
API_KEY='sua_chave_api_google_gen_ai'
HUGGINGFACE_KEY='sua_chave_api_hugging_face'
```
### Uso
Para executar o aplicativo, use o seguinte comando no diretório do script:
```
streamlit run seu_script.py
```
O aplicativo permite ao usuário fazer upload de uma imagem em formato JPG. Após o processamento, o texto extraído é convertido em fala e pode ser reproduzido diretamente na interface do Streamlit.

##Estrutura do Código
* Importação de Bibliotecas: Importa os módulos necessários.
* Carregamento das Variáveis de Ambiente: Carrega as chaves de API do arquivo .env.
* Funções de Conversão:
    * image_to_text(image_path): Converte uma imagem em texto.
    * story_to_speech(story): Converte o texto em áudio.
* Função Principal (main): Configura a página do Streamlit e gerencia o upload e processamento da imagem.
* Execução: Inicia o aplicativo se o script é o módulo principal.



# Objetivos Futuros 
- Este trabalho serve como um projeto para entendimento inicial do uso das ferramentas.
- O objeitvo principal é utilziar as ferramentas de Image-To-Text, para a descrição do ambiente para pessoas cegas, como ferramenta de suporte.
- Servindo como descrição do Ambiente, Posição espacial, entre demais opções

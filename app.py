import os
from dotenv import load_dotenv
import streamlit as st
import requests
from PIL import Image
import io
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv('API_KEY')
HUGGINGFACE_KEY = os.getenv('HUGGINGFACE_KEY')
genai.configure(api_key=API_KEY)

def image_to_text(image_path):
    model = genai.GenerativeModel('gemini-pro-vision')
    # Carregar a imagem e garantir que ela não dependa do arquivo
    with open(image_path, "rb") as image_file:
        image = Image.open(image_file)
        image = image.copy()  # Cria uma cópia da imagem que não depende do arquivo

    # Tentativa de usar diretamente o objeto Image
    response = model.generate_content(["You are an assistant designed to help people with visual impairments. Your task is to identify and describe objects in an image, geographically locate each item within the image (for example, on the left, in the center, on the right), and highlight any potentially dangerous conditions such as holes, steps, or dangerous animals. Provide a detailed and clear description of the overall scene in the image, mentioning important points of interest and attention. Do not use the expression (the image shows), you are describing what is in front of the user", image], stream=True)
    response.resolve()
    return response.text

def story_to_speech(story):
    API_URL = 'https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits'
    headers = {"Authorization": f'Bearer {HUGGINGFACE_KEY}'}
    payload = {"inputs": story}
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio-img/story_speech.flac', 'wb') as file:
        file.write(response.content)

def main():
    st.set_page_config(page_title="Conversor de Imagem para Áudio", page_icon="🖼️")
    st.header("Image to Audio Description Converter")
    file_upload = st.file_uploader("Please upload a jpg image here", type="jpg")
    if file_upload is not None:
        image_path = f'audio-img/{file_upload.name}'
        with open(image_path, "wb") as file:
            file.write(file_upload.getvalue())
        st.image(file_upload, caption="Uploaded Image")
        text = image_to_text(image_path)
        if text:
            story_to_speech(text)
            with st.expander('Generated Image Description'):
                st.write(text)
            st.audio('audio-img/story_speech.flac')
        else:
            st.error("Failed to generate text from the image.")
    else:
        st.warning("Please upload an image to generate a story.")

if __name__ == '__main__':
    main()

from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fundtion to load Gemini Pro model and get respone
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_reponse(input, query):
    if(input != ""):
        reponse=model.generate_content([input, query])
    else:
        reponse=model.generate_content(query)
    return reponse.text

## initialize out steamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")

uploadFile = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploadFile is not None:
    image = Image.open(uploadFile)
    st.image(image, caption="Upload Image", use_column_width=True)

submit=st.button("Tell me about the image")

## if submit is clicked,
if submit:
    respone=get_gemini_reponse(input, image)
    st.subheader("The Response is")
    st.write(respone)





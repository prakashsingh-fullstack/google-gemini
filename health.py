### Health Management APP
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Funcation to load Google Gemini Pro Vision API get Respone

def get_gemini_response(input, image, propmt):
    model=genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, image[0], propmt])
    return response.text

## get an image byte data
def input_image_setup(uploaded_file):
    #check if a file has been uploaded
    if uploaded_file is not None:
        #Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")
    
## initialize the streamlit app
st.set_page_config(page_title="Daily Health Information")
st.header("Health Application")
input = st.text_input("Input Prompt ", key="input")
uploadedFile = st.file_uploader("Choose an image.. ", type=["jpg","jpeg","png"])
image = ""
if uploadedFile is not None:
    image = Image.open(uploadedFile)
    st.image(image, caption="Uploaded image", use_column_width=True)

submit = st.button("Tell me total calories")

input_prompt = """
    You are an expert in nutritionist where you need to see the food items from the image and calculate the total calories,
    also provide the details of every food items with calories intake in the below format:
    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ----
    ----
"""

# if the submit button is clicked
if submit:
    image_data = input_image_setup(uploadedFile)
    response = get_gemini_response(input_prompt,image_data, input)
    st.header("The Reponse is : ")
    st.write(response)






from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fundtion to load Gemini Pro model and get respone
model=genai.GenerativeModel("gemini-pro")
def get_gemini_reponse(query):
    reponse=model.generate_content(query)
    return reponse.text

## initialize out steamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Applications")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask me Question")

## when submit is clicked

if submit:
    response=get_gemini_reponse(input)
    st.subheader("The Response is")
    st.write(response)

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_reponse(query):
    response = chat.send_message(query, stream=True)
    return response

## initialize streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

## Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the Question?")

if submit and input:
    reponse = get_gemini_reponse(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The reponse is ")
    for chunk in reponse:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("The chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")



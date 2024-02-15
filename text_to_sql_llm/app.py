from dotenv import load_dotenv
load_dotenv() # load environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
##configure API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Function to load google gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

## functoin to retrieve query from the sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define the Prompt
prompt ="""
    You are an expert in converting English question to SQL Query!
    The SQL database has the name STUDENT and has the following Column - NAME, CLASS, SECTION and MARKS \n\nFor Example,
    \nExample 1- How many entries of the records are present in the database?, the SQL command will be something like this
    SELECT COUNT(*) FROM STUDENT ;\nExample 2 Tell me all the students studying in Web Developer class?, 
    the SQL command will be something like this SELECT * from STUDENT where CLASS = "Web Developer";
    also the SQL code should not have ``` in the beginning or end and the sql world in the output
"""
## streamlit app 
st.set_page_config(page_title="I Can retrive any SQL query")
st.header("Gemini APP to Retrive SQL Data")
question = st.text_input("Input: ",key="input")
submit = st.button("Ask the Question")

# if submit is clicked

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for student in data:
        print(student)
        st.header(student)
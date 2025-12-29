from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.5-flash")

def my_output(query):
    response=model.generate_content(query)
    return response.text

st.set_page_config(page_title='Chat with Gemini-2.5', page_icon=':robot_face:')
st.header('Chat with Gemini-2.5 :robot_face:')
input=st.text_input('input', key='input')
submit=st.button('Submit')

if submit:
    response=my_output(input)
    st.subheader('Response:')
    st.write(response)
    
import streamlit as st
import os
import google.generativeai as genai

with open('gemini_api.txt','r') as f:
    api_key = f.read()
    genai.configure(api_key = api_key)

st.title('AI Code Reviewer')
system_prompt = '''Assume you are a code reviewer. People will share their code with
you and ask you to find the errors in their code. if there are errors in code you have
to suggest them changes, should correct their code and also generate correct code. if there is no error just ask them what
changes they want in their code. Also suggestions given by you should be polite, beginner friendly 
, information should be factual and in points. If the user something different from the code then politely reject their request.'''
model = genai.GenerativeModel(model_name = 'models/gemini-2.0-flash-exp',system_instruction = system_prompt)    


user = st.text_area('Enter your code here: ')
if st.button('Submit'):
    response = model.generate_content(user)
    st.write(response.text)
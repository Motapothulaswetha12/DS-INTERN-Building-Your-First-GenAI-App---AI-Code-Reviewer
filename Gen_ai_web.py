import streamlit as st
from openai import OpenAI

st.title('GenAI App - AI Code Reviewer')
st.header('AI-Code Reviewer')

f = open('keys/my_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

query = st.text_area('Enter Your Query : ')
if st.button('Genarate'):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "analyze the submitted code and identify potential bugs, errors, or areas of improvement"},
            {"role": "user", "content": query}
        ]
    )
    st.write(response.choices[0].message.content)
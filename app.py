import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#load environment variables
load_dotenv()
#Get the hugging face api token from the environment
groq_api_key = os.getenv("GROQ_API_KEY")

system ="You are an Al assistant that specializes in providing clear concise and accurate responses Be polite and only provide relevant answers and descriptions where needed"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "question: {question}")
    ]
)
#A function to generate respponse

def generate_response(question, engine, temperature, max_token):
    llm = ChatGroq(groq_api_key=groq_api_key, model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

st.title("QA CHATBOT")
engine =st.sidebar.selectbox("Select Model", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "meta-llama/llama-4-maverick-17b-128e-instruct","meta-llama/llama-4-scout-17b-16e-instruct","qwen/qwen3-32b","openai/gpt-oss-120b"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value = 0.7)
max_token = st.sidebar.slider("Max token", min_value=50, max_value= 300, value=150)


#st.write("Please enter your question")
user_input = st.text_input("Please enter your question:", "")

if st.button("send"):
    response = generate_response(user_input, engine, temperature, max_token)
    st.text_area ("Al response:", value=response, height=300)
#else:
    #st.write("Please enter your question")
    
st.markdown("This Chatbot  was designed by Dhipzy")    

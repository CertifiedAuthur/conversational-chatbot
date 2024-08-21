import streamlit as st
import openai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()

# Streamlit UI
st.title("Conversational Q&A Chatbot")
st.header("Hey, Let's chat")

# Sidebar input for OpenAI API key
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Function to initialize the ChatOpenAI object with user-provided API key
def initialize_chat_model(api_key):
    return ChatOpenAI(openai_api_key=api_key, temperature=0.5)

# Initialize conversation history in session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI assistant')
    ]

# Function to get response from the chat model
def get_chatmodel_response(question, api_key):
    chat = initialize_chat_model(api_key)
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# Button to set API key and initialize chat model
if st.sidebar.button("Set API Key"):
    if api_key:
        st.success("API Key set successfully!")
    else:
        st.warning("Please enter your OpenAI API Key.")

# Check if the API key is set and not empty
if api_key:
    input = st.text_input("Input: ", key="input")
    if st.button("Ask the question"):
        response = get_chatmodel_response(input, api_key)
        st.subheader("The Response is")
        st.write(response)
else:
    st.info("Please enter your OpenAI API Key in the sidebar.")

import streamlit as st
import openai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit UI setup
st.title("Conversational Q&A Chatbot")
st.header("Hey, Let's chat")

# Initialize the ChatOpenAI object
chat = ChatOpenAI(temperature=0.5)

# Initialize conversation history in session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI assistant')
    ]

# Sidebar input for OpenAI API key
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Function to set the OpenAI API key
def set_api_key(key):
    openai.api_key = key

# Button to set API key
if st.sidebar.button("Enter"):
    if api_key:
        set_api_key(api_key)
        st.success("API Key set successfully!")
    else:
        st.warning("Please enter your OpenAI API Key.")

# Check if the API key is set before processing input
if api_key:
    # Text input for user query
    user_input = st.text_input("Input:", key="input")

    # Function to get the chatbot response
    def get_chatmodel_response(question):
        st.session_state['flowmessages'].append(HumanMessage(content=question))
        answer = chat(st.session_state['flowmessages'])
        st.session_state['flowmessages'].append(AIMessage(content=answer.content))
        return answer.content

    # Button to submit the question
    submit = st.button("Ask the question")

    # If submit button is clicked, display the response
    if submit and user_input:
        response = get_chatmodel_response(user_input)
        st.subheader("The Response is:")
        st.write(response)
else:
    st.warning("Please enter your OpenAI API Key in the sidebar.")

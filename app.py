import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import StreamlitCallbackHandler
import os

DB_PATH = "sales.db"

if not os.path.exists(DB_PATH):
    st.error(
        f"Database file not found at '{DB_PATH}'. "
        "Please run `init_db.py` to create and initialize the database before using this app."
    )
    st.stop()

st.set_page_config(page_title="Agent Demo", page_icon="🤖")
st.title("Demo: Text-to-SQL Agent")
st.markdown("""
**Purpose:** This agent connects to a local SQL database and allows users to query data using natural language.  
**Tech Stack:** Python, LangChain, SQLite, OpenAI GPT-3.5.
""")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
api_key = api_key.strip() if api_key else ""
if not api_key:
    st.info("Please enter your OpenAI API key in the sidebar to start.")
    st.stop()
if not api_key.startswith("sk-"):
    st.error("The API key you entered doesn't look like a valid OpenAI key. It should start with 'sk-'. Please double-check and try again.")
    st.stop()

db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")

# Temperature=0 is critical here to ensure the LLM generates deterministic SQL queries, not creative text.
if (
    "agent_executor" not in st.session_state
    or st.session_state.get("api_key") != api_key
):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        api_key=api_key,
    )
    st.session_state["agent_executor"] = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=True,
    )
    st.session_state["api_key"] = api_key
agent_executor = st.session_state["agent_executor"]

st.write("---")
st.write("### Ask a question about the dummy data:")
st.write("*(Try: 'How many employees are in the Sales department?' or 'What is the total revenue from Enterprise Licenses?')*")

user_query = st.text_input("Your Question:")

if user_query:
    with st.spinner("Agent is thinking..."):
        try:
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent_executor.invoke(
                {"input": user_query}, 
                {"callbacks": [st_callback]} 
            )
            st.success(response["output"])
        except Exception as e:
            st.error(f"An error occurred")
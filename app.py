import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

DB_PATH = "sales.db"

st.set_page_config(page_title="Agent Demo", page_icon="🤖")
st.title("Demo: Text-to-SQL Agent")
st.markdown("""
**Purpose:** This agent connects to a local SQL database and allows users to query data using natural language.  
**Tech Stack:** Python, LangChain, SQLite, OpenAI GPT-3.5.
""")

db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if not api_key:
    st.info("Please enter your OpenAI API key in the sidebar to start.")
    st.stop()

# Temperature=0 is critical here to ensure the LLM generates deterministic SQL queries, not creative creative text.
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0, 
    api_key=api_key
)

agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True
)

st.write("---")
st.write("### Ask a question about the dummy data:")
st.write("*(Try: 'How many employees are in the Sales department?' or 'What is the total revenue from Enterprise Licenses?')*")

user_query = st.text_input("Your Question:")

if user_query:
    with st.spinner("Agent is thinking..."):
        try:
            response = agent_executor.invoke(user_query)
            st.success(response["output"])
            
            with st.expander("See technical details (SQL Logic)"):
                st.write("The agent generated and executed SQL based on your question.")
        except Exception as e:
            st.error(f"An error occurred: {e}")